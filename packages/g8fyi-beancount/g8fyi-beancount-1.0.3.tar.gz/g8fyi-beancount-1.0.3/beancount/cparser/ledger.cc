#include "beancount/cparser/ledger.h"

#include "beancount/ccore/std_utils.h"
#include "beancount/ccore/number.h"
#include "beancount/utils/errors.h"
#include "beancount/ccore/precision.h"

#include "absl/status/status.h"
#include "absl/strings/str_format.h"
#include "absl/strings/str_cat.h"
#include "google/protobuf/io/zero_copy_stream.h"
#include "google/protobuf/io/zero_copy_stream_impl.h"
#include "google/protobuf/text_format.h"

#include <functional>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

namespace beancount {
using absl::StrFormat;
using google::protobuf::io::ZeroCopyOutputStream;
using google::protobuf::io::FileOutputStream;
using google::protobuf::TextFormat;

static int kDefaultDecimalPrecision = 28;

Ledger::~Ledger() {
  for (auto* directive : directives) delete directive;
  for (auto* error : errors) delete error;
}

absl::Status WriteToText(const Ledger& ledger, const std::string& filename) {
  // Open output file.
  int outfd = open(filename.c_str(), O_CREAT|O_WRONLY|O_TRUNC, S_IRUSR|S_IWUSR);
  if (outfd == -1) {
    return SystemError(absl::StrCat("Error opening file '", filename, "'"));
  }
  ZeroCopyOutputStream* output = new FileOutputStream(outfd);

  // Output directives.
  for (const auto& dir : ledger.directives) {
    LedgerProto ledger_proto;
    ledger_proto.add_directives()->CopyFrom(*dir);
    if (!TextFormat::Print(ledger_proto, output)) {
      return SystemError(absl::StrCat("Error writing out message to '", filename, "'"));
    }
  }

  // Output errors, options and processing info.
  LedgerProto ledger_proto;
  for (const auto& error : ledger.errors) {
    ledger_proto.add_errors()->CopyFrom(*error);
  }
  ledger_proto.mutable_options()->CopyFrom(*ledger.options);
  ledger_proto.mutable_info()->CopyFrom(*ledger.info);

  if (!TextFormat::Print(ledger_proto, output)) {
    return SystemError(absl::StrCat("Error writing out message to '", filename, "'"));
  }

  // Close output.
  delete output;
  if (close(outfd) == -1) {
    return SystemError(absl::StrCat("Error closing file '", filename, "'"));
  }

  return absl::OkStatus();
}

std::unique_ptr<inter::Ledger> LedgerToProto(const Ledger& ledger) {
  auto output = std::make_unique<inter::Ledger>();
  for (const auto* dir : ledger.directives) {
    output->add_directives()->CopyFrom(*dir);
  }
  for (const auto* error : ledger.errors) {
    output->add_errors()->CopyFrom(*error);
  }
  if (ledger.options->ByteSizeLong() > 0) {
    output->mutable_options()->CopyFrom(*ledger.options);
  }
  if (ledger.info->ByteSizeLong() > 0) {
    output->mutable_info()->CopyFrom(*ledger.info);
  }
  return output;
}

void AddError(Ledger* ledger, std::string_view message, const Location& location) {
  auto* error = new Error();
  ledger->errors.push_back(error);
  error->set_message(Capitalize(message));
  error->mutable_location()->CopyFrom(location);
}

decimal::Decimal EvaluateExpression(const inter::Expr& expr, decimal::Context& context) {
  switch (expr.op()) {
    case inter::ExprOp::NUM: {
      return ProtoToDecimalOrDie(expr.number());
    }
    case inter::ExprOp::ADD: {
      auto num1 = EvaluateExpression(expr.arg1(), context);
      auto num2 = EvaluateExpression(expr.arg2(), context);
      return num1.add(num2, context);
    }
    case inter::ExprOp::SUB: {
      auto num1 = EvaluateExpression(expr.arg1(), context);
      auto num2 = EvaluateExpression(expr.arg2(), context);
      return num1.sub(num2, context);
    }
    case inter::ExprOp::MUL: {
      auto num1 = EvaluateExpression(expr.arg1(), context);
      auto num2 = EvaluateExpression(expr.arg2(), context);
      return num1.mul(num2, context);
    }
    case inter::ExprOp::DIV: {
      auto num1 = EvaluateExpression(expr.arg1(), context);
      auto num2 = EvaluateExpression(expr.arg2(), context);
      return num1.div(num2, context);
    }
    case inter::ExprOp::NEG: {
      auto num1 = EvaluateExpression(expr.arg1(), context);
      return num1.minus(context);
    }
    case inter::ExprOp::PLUS:
    case inter::ExprOp::PAREN: {
      return EvaluateExpression(expr.arg1(), context);
    }
    default:
      // Invalid value.
      assert(false);
  }
}

// Reduce an expression to its corresponding number, mutating the input proto.
template <typename T>
void ReduceExpression(T* parent,
                      decimal::Context& context,
                      DecimalConversion conversion) {
  if (!parent->has_expr())
    return;
  decimal::Decimal number = EvaluateExpression(parent->expr(), context);
  auto status = DecimalToProto(number,
                               conversion,
                               parent->mutable_number());
  assert(status.ok());
  parent->clear_expr();
}

template void ReduceExpression(inter::PriceSpec* parent,
                               decimal::Context& context,
                               DecimalConversion conversion);
template void ReduceExpression(inter::UnitSpec* parent,
                               decimal::Context& context,
                               DecimalConversion conversion);
template void ReduceExpression(inter::ExprNumber* parent,
                               decimal::Context& context,
                               DecimalConversion conversion);
template void ReduceExpression(Amount* parent,
                               decimal::Context& context,
                               DecimalConversion conversion);

void ReduceExpressions(Ledger* ledger,
                       decimal::Context& context,
                       DecimalConversion decimal_conversion,
                       beancount::Directive* directive) {
  if (directive->has_transaction()) {
    // Transaction directive.
    for (auto& posting : *directive->mutable_transaction()->mutable_postings()) {
      if (posting.has_spec()) {
        // Evaluate units.
        auto* spec = posting.mutable_spec();
        if (spec->has_units()) {
          ReduceExpression(spec->mutable_units(), context, decimal_conversion);
        }

        if (spec->has_cost()) {
          // Evaluate per-unit cost.
          auto* cost = spec->mutable_cost();
          if (cost->has_per_unit()) {
            ReduceExpression(cost->mutable_per_unit(), context, decimal_conversion);
          }
          // Evaluate total cost.
          if (cost->has_total()) {
            ReduceExpression(cost->mutable_total(), context, decimal_conversion);
          }
        }

        // Evaluate price annotation.
        if (spec->has_price()) {
          auto* price = spec->mutable_price();
          ReduceExpression(price, context, decimal_conversion);

          // Prices may not be negative. Check and issue an error if found; fix up
          // the price to its absolute value and continue.
          if (price->has_number()) {
            decimal::Decimal dec = ProtoToDecimalOrDie(price->number());
            if (dec.sign() == -1) {
              AddError(ledger,
                       "Negative prices are not allowed "
                       "(see http://furius.ca/beancount/doc/bug-negative-prices "
                       "for workaround)", directive->location());
              // Invert and continue.
              auto status = DecimalToProto(-dec, decimal_conversion,
                                           price->mutable_number());
              assert(status.ok());
            }
          }
        }
      }
    }
  } else if (directive->has_price()) {
    // Price directive.
    auto* price = directive->mutable_price();
    if (price->has_amount()) {
      ReduceExpression(price->mutable_amount(), context, decimal_conversion);
    }
  } else if (directive->has_balance()) {
    // Balance directive.
    auto* balance = directive->mutable_balance();
    if (balance->has_amount()) {
      ReduceExpression(balance->mutable_amount(), context, decimal_conversion);
    }
  }
}

void NormalizeTotalPrices(Ledger* ledger,
                          decimal::Context& context,
                          DecimalConversion decimal_conversion,
                          beancount::Directive* directive) {
  if (!directive->has_transaction())
    return;

  for (auto& posting : *directive->mutable_transaction()->mutable_postings()) {
    if (posting.has_spec() && posting.spec().has_price()) {
      auto* spec = posting.mutable_spec();
      auto* price = spec->mutable_price();

      // Expressions should have already been evaluated.
      assert(!price->has_expr());

      // If the price is specified for the entire amount, we process it.
      bool is_total_price = price->is_total();
      price->clear_is_total();
      if (is_total_price) {
        if (spec->has_units() && spec->units().has_number()) {
          // Expressions should have already been evaluated.
          assert(!spec->units().has_expr());

          // We compute the effective price here and forget about that detail of
          // the input syntax.
          decimal::Decimal dunits = ProtoToDecimalOrDie(spec->units().number());
          decimal::Decimal dprice;
          if (dunits.iszero()) {
            dprice = dunits;
          } else {
            dprice = ProtoToDecimalOrDie(price->number()).div(dunits.abs(), context);
          }
          auto status = DecimalToProto(dprice,
                                       decimal_conversion,
                                       price->mutable_number());
          assert(status.ok());
        } else {
          // units.number is MISSING, issue and error and clear the price.
          //
          // Note that we could potentially do a better job and attempt to
          // perform the normalization after an attempt at interpolation, but
          // this situation is pretty rare anyway.
          AddError(ledger,
                   StrFormat("Total price on a posting without units: %s.",
                             price->DebugString()), posting.location());
          spec->clear_price();
        }
      }
    }
  }
}

void CheckCoherentCurrencies(Ledger* ledger,
                             beancount::Directive* directive) {
  if (!directive->has_transaction())
    return;

  for (auto& posting : *directive->mutable_transaction()->mutable_postings()) {
    const auto& spec = posting.spec();
    if (spec.has_cost() && spec.has_price()) {
      const auto& cost = spec.cost();
      const auto& price = spec.price();
      if (cost.has_currency() &&
          price.has_currency() &&
          spec.cost().currency() != price.currency()) {
        AddError(ledger, StrFormat("Cost and price currencies must match: %s != %s",
                                   cost.currency(), price.currency()), posting.location());
      }
    }
    // Note: We allow zero prices because we need them for round-trips for
    // conversion entries.
  }
}

void RemoveDuplicateMetaKeys(Ledger* ledger, Meta* meta, const Location& location) {
  std::set<std::string> keys;
  auto* kvs = meta->mutable_kv();
  for (auto iter = kvs->begin(); iter != kvs->end(); ) {
    if (!iter->key().empty() && !keys.insert(iter->key()).second) {
      AddError(ledger, StrFormat("Duplicate metadata key: '%s' with value '%s'",
                                 iter->key(), iter->value().DebugString()), location);
      iter = kvs->erase(iter);
    } else {
      ++iter;
    }
  }
}

void RemoveDuplicateMetaKeys(Ledger* ledger, Directive* directive) {
  if (directive->has_meta()) {
    RemoveDuplicateMetaKeys(ledger, directive->mutable_meta(), directive->location());
  }
  if (directive->has_transaction()) {
    for (auto& posting : *directive->mutable_transaction()->mutable_postings()) {
      if (posting.has_meta() ) {
        RemoveDuplicateMetaKeys(ledger, posting.mutable_meta(), posting.location());
      }
    }
  }
}

void PostProcessParsed(Ledger* ledger,
                       DecimalConversion decimal_conversion,
                       bool normalize_totals,
                       bool allow_multi_meta) {
  // Set Decimal context before processing, update the desired precision for
  // arithmetic operations.
  decimal::Context context = decimal::context;
  context.prec(ledger->options->has_decimal_evaluation_precision() ?
               ledger->options->decimal_evaluation_precision() :
               kDefaultDecimalPrecision);

  // Process all the directives.
  PrecisionStatsAccum stats;
  using namespace std::placeholders;
  for (auto* directive : ledger->directives) {
    // Reduce all expressions in a given context.
    ReduceExpressions(ledger, context, decimal_conversion, directive);

    // Update the precision statistics accumulator.
    UpdateStatistics(*directive, &stats);

    // Normalize total price to unit price.
    if (normalize_totals) {
      NormalizeTotalPrices(ledger, context, decimal_conversion, directive);
    }

    // Run checks on currencies between cost and prices.
    CheckCoherentCurrencies(ledger, directive);

    // Remove duplicate keys in meta-data.
    if (!allow_multi_meta) {
      RemoveDuplicateMetaKeys(ledger, directive);
    }
  }
}

}  // namespace beancount
