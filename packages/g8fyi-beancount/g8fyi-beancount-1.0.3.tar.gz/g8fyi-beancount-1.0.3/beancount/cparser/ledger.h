// Parsed and booked state of a ledger. This is the main artifact produced by
// the Beancount core. This is mainly a list of directives, and some side-state.
//
// Copyright (C) 2020  Martin Blais
// License: "GNU GPLv2"

#ifndef BEANCOUNT_CPARSER_LEDGER_H_
#define BEANCOUNT_CPARSER_LEDGER_H_

#include "beancount/cparser/ledger.pb.h"

#include <list>
#include <memory>
#include <string>
#include <string_view>
#include <vector>

#include "beancount/cparser/options.pb.h"
#include "beancount/cparser/inter.pb.h"
#include "beancount/ccore/data.pb.h"
#include "beancount/ccore/number.h"

#include "decimal.hh"
#include "absl/status/status.h"

namespace beancount {

// Container for all data produced by the parser, and also by Beancount in
// general (after booking, interpolation, and plugins processing).
//
// Note that this a C++ container; we also have a separate proto container used
// for tests.
struct Ledger final {
  ~Ledger();

  // A list of directives, with ownership.
  std::list<Directive*> directives;

  // A list of errors encountered during parsing and processing.
  std::vector<Error*> errors;

  // Parsed options.
  std::shared_ptr<options::Options> options;

  // Processing details.
  std::shared_ptr<options::ProcessingInfo> info;
};

// Write ledger content to a text-formatted file.
absl::Status WriteToText(const Ledger& ledger, const std::string& filename);

// Convert the class above to a proto version.
std::unique_ptr<inter::Ledger> LedgerToProto(const Ledger& ledger);

// Add an error to the ledger.
void AddError(Ledger* ledger, std::string_view message, const Location& location);

// Evaluate an expression without modifying the proto.
decimal::Decimal EvaluateExpression(const inter::Expr& expr,
                                    decimal::Context& context);

// Evaluate all the expressions to their numbers in a directive.
// This essentially performs all the supported arithmetic evaluation.
void ReduceExpressions(Ledger* ledger,
                       decimal::Context& context,
                       DecimalConversion conversion,
                       Directive* directive);

// Reduce the total price of a posting with price to per-unit price.
void NormalizeTotalPrices(Ledger* ledger,
                          decimal::Context& context,
                          DecimalConversion conversion,
                          Directive* directive);

// If both cost and price are specified, check that the currencies must match.
void CheckCoherentCurrencies(Ledger* ledger,
                             Directive* directive);

// Remove convert duplicate metadata keys to errors.
void RemoveDuplicateMetaKeys(Ledger* ledger, Directive* directive);

// Process the parsed contents of a ledger.
void PostProcessParsed(Ledger* ledger,
                       DecimalConversion conversion,
                       bool normalize_totals,
                       bool allow_multi_meta);

}  // namespace beancount

#endif // BEANCOUNT_CPARSER_LEDGER_H_
