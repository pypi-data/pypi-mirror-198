#include "beancount/cparser/builder.h"

#include "beancount/ccore/account.h"
#include "beancount/ccore/account_types.h"
#include "beancount/ccore/std_utils.h"

#include <filesystem>
#include <optional>

#include "absl/status/status.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_format.h"
#include "absl/strings/str_join.h"
#include "absl/strings/str_split.h"
#include "google/protobuf/descriptor.pb.h"
#include "google/protobuf/text_format.h"
#include "re2/re2.h"

namespace beancount {
namespace parser {
namespace filesystem = std::filesystem;
using absl::StrFormat;
using google::protobuf::FieldDescriptor;
using google::protobuf::TextFormat;
using std::string;

// NOTE(blais): You could set_allocate_expr() in this function and avoid a copy
// and allocation/delete in the caller.
template <typename T>
void SetExprOrNumber(T* parent,
                     const inter::Expr& expr) {
  // Set the value immediately if possible.
  assert(parent != nullptr);

  // If set and reducible trivially to a number, reduce now.
  if (expr.op() == inter::ExprOp::NUM) {
    assert(expr.has_number());
    assert(!expr.has_arg1());
    assert(!expr.has_arg2());
    parent->mutable_number()->CopyFrom(expr.number());
  } else {
    // Otherwise, copy as expression.
    assert(expr.has_arg1());
    assert(!expr.has_number());
    parent->mutable_expr()->CopyFrom(expr);
  }
}

template void SetExprOrNumber(inter::UnitSpec* parent, const inter::Expr& expr);
template void SetExprOrNumber(inter::PriceSpec* parent, const inter::Expr& expr);
template void SetExprOrNumber(inter::ExprNumber* parent, const inter::Expr& expr);
template void SetExprOrNumber(Amount* parent, const inter::Expr& expr);

Builder::Builder(scanner::Scanner& scanner) :
  scanner_(scanner)
{
  info_.reset(new options::ProcessingInfo());
  options_.reset(new options::Options());
}

Builder::~Builder() {
  for (auto* directive : directives_) delete directive;
  for (auto* error : errors_) delete error;
}

void Builder::AddOptionBinary(const string& key, string&& value, const location& loc) {
  string value_str = std::move(value);

  // Translate legacy option names to proto equivalents.
  static std::vector<std::pair<const char*, const char*>> translations = {
    {"name_assets",       "account_types { assets: '%s' }"},
    {"name_liabilities",  "account_types { liabilities: '%s' }"},
    {"name_income",       "account_types { income: '%s' }"},
    {"name_expenses",     "account_types { expenses: '%s' }"},
    {"name_equity",       "account_types { equity: '%s' }"},
  };
  for (const auto& translation : translations) {
    if (key == translation.first) {
      char buffer[1024];
      if (std::snprintf(buffer, 1024, translation.second, value_str.c_str()) >= 1024) {
        AddError(StrFormat("String too large for options: '%s'", value_str), loc);
        return;
      }
      return AddOptionUnary(buffer, loc);
    }
  }

  // Check the options field and get relevant descriptors.
  const auto* descriptor = options_->GetDescriptor();
  const auto* field = descriptor->FindFieldByName(key);
  if (!field) {
    AddError(StrFormat("Invalid option: '%s'", key), loc);
    return;
  }

  // Issue a warning if the option is deprecated.
  if (field->options().deprecated()) {
    AddError(StrFormat("Option '%s' is deprecated; ignored.", key), loc);
    return;
  }

  // Preprocess fields which are intended for mappings.
  // This is essentially for backward compatibility for "inferred_tolerance_default".
  if (field->is_map()) {
    std::vector<string> components = absl::StrSplit(value_str, ":");
    if (components.size() != 2) {
      AddError(StrFormat("Invalid format for '%s': '%s'", key, value_str), loc);
      return;
    }
    value_str = absl::StrFormat("{ key: '%s' value: '%s' }", components[0], components[1]);
  }

  // Set the field on the options proto. Note that if the field is a repeated
  // field, the ParseFieldValueFromString() method correctly appends to the list
  // of existing values.
  if (field->type() == FieldDescriptor::TYPE_STRING) {
    value_str = absl::StrCat("\"", absl::CEscape(value_str), "\"");
  }
  if (!TextFormat::ParseFieldValueFromString(value_str, field, options_.get())) {
    AddError(StrFormat("Could not parse and set option '%s' with value '%s'; ignored.",
                       key, value_str), loc);
    return;
  }
}

void Builder::AddOptionUnary(const string& proto_str, const location& loc) {
  if (!TextFormat::MergeFromString(proto_str, options_.get())) {
    AddError(StrFormat("Could not parse and merge options proto with value '%s'; ignored.",
                       proto_str), loc);
    return;
  }
}

void Builder::AddInclude(string&& filename) {
  info_->add_include(filename);
}

void Builder::AddPlugin(string&& name, const absl::optional<string>& config) {
  auto* plugin = info_->add_plugin();
  plugin->set_name(name);
  if (config.has_value()) {
    plugin->set_config(std::move(config.value()));
  }
}

const string& Builder::InternAccount(string&& account, const location& loc) {
  auto iter = accounts_.insert(std::make_pair(account, loc));
  return (*iter.first).first;
}

string Builder::MakeAbsolutePath(const string& filename) {
  if (!filename.empty()) {
    filesystem::path document_path(filename);
    if (document_path.is_relative()) {
      const string* filename = scanner_.location().begin.filename;
      assert(filename);
      filesystem::path parser_filename(*filename);
      return parser_filename.parent_path() / document_path;
    }
  }
  return string(filename);
}


void Builder::SetTagsAndLinks(const TagsLinks* tags_links, Directive* message) const {
  if (!active_tags_.empty()) {
    // First copy the active tags.
    auto* output = message->mutable_tags();
    for (const auto& active_tag : active_tags_) {
      *output->Add() = active_tag;
    }
  }

  if (tags_links != nullptr) {
    // Add the new tags.
    if (!tags_links->tags.empty()) {
      // Avoiding duplicates with active metadata.
      for (const auto& tag : tags_links->tags) {
        if (active_tags_.find(tag) == active_tags_.end()) {
          *message->mutable_tags()->Add() = tag;
        }
      }
    }

    // Add the new links.
    if (!tags_links->links.empty()) {
      auto* output = message->mutable_links();
      for (const auto& link : tags_links->links) {
        *output->Add() = link;
      }
    }
  }
}

void Builder::PushTag(const string& tag) {
  active_tags_.insert(tag);
}

void Builder::PopTag(const string& tag, const location& loc) {
  auto iter = active_tags_.find(tag);
  if (iter != active_tags_.end()) {
    active_tags_.erase(iter);
  } else {
    AddError(StrFormat("Attempting to pop absent tag: '%s'", tag), loc);
  }
}

void Builder::PushMeta(std::string_view key, MetaValue* value) {
  auto& value_list = active_meta_[key];
  value_list.push_back(value);
}

void Builder::PopMeta(const string& key, const location& loc) {
  auto iter = active_meta_.find(key);
  if (iter == active_meta_.end()) {
    AddError(StrFormat("Attempting to pop absent metadata key: '%s'", key), loc);
  } else {
    auto& value_list = iter->second;
    assert(value_list.size() > 0);
    auto* value = value_list.back();
    value_list.pop_back();
    if (value_list.empty()) {
      active_meta_.erase(iter);
    }
    delete value;
  }
}

void Builder::AddActiveMetadata(Meta* meta, Directive* dir) const {
  // Append active metadata into the output.
  if (!active_meta_.empty()) {
    Meta* dirmeta = dir->mutable_meta();
    for (auto [key, value_list] : active_meta_) {
      auto* kv = dirmeta->mutable_kv()->Add();
      kv->set_key(key);
      kv->mutable_value()->CopyFrom(*value_list.back());
    }
  }

  // Merge given metadata on top of active metadttaa.
  if (meta != nullptr) {
    Meta* dirmeta = dir->mutable_meta();
    dirmeta->MergeFrom(*meta);
  }
}

absl::Status Builder::MergeCost(const inter::CostSpec& new_cost_spec, inter::CostSpec* accumulator) {
  if (new_cost_spec.has_per_unit() && accumulator->has_per_unit()) {
    return absl::InvalidArgumentError("Duplicate `per_unit` cost spec field.");
  }
  if (new_cost_spec.has_total() && accumulator->has_total()) {
    return absl::InvalidArgumentError("Duplicate `total` cost spec field.");
  }
  if (new_cost_spec.has_currency() && accumulator->has_currency()) {
    return absl::InvalidArgumentError("Duplicate `currency` cost spec field.");
  }
  if (new_cost_spec.has_date() && accumulator->has_date()) {
    return absl::InvalidArgumentError("Duplicate `date` cost spec field.");
  }
  if (new_cost_spec.has_label() && accumulator->has_label()) {
    return absl::InvalidArgumentError("Duplicate `label` cost spec field.");
  }
  if (new_cost_spec.has_merge_cost() && accumulator->has_merge_cost()) {
    return absl::InvalidArgumentError("Duplicate `merge_cost` cost spec field.");
  }

  accumulator->MergeFrom(new_cost_spec);
  return absl::OkStatus();
}

Directive* Builder::MakeDirective(const absl::CivilDay& date,
                                  Meta** meta,
                                  TagsLinks** tags_links) const {
  auto* dir = new Directive();

  // Set the date.
  DateToProto(date, dir->mutable_date());

  // Copy the metadata, if provided, including the stack's metadata.
  Meta* ourmeta = nullptr;
  if (meta != nullptr) {
    ourmeta = *meta;
    meta = nullptr;
  }
  AddActiveMetadata(ourmeta, dir);
  delete ourmeta;

  // Update tags, including adding active tags, and links.
  if (tags_links != nullptr) {
    SetTagsAndLinks(*tags_links, dir);
    if (*tags_links != nullptr) {
      delete *tags_links;
      *tags_links = nullptr;
    }
  }

  return dir;
}

void Builder::AppendDirective(Directive* directive) {
  directives_.push_back(directive);
}

void Builder::PreparePosting(Posting* posting,
                             const inter::Expr* maybe_expr,
                             const absl::optional<string>& maybe_currency,
                             const char flag,
                             const string& account,
                             bool is_total_price,
                             const location& loc) {
  assert(posting != nullptr);

  // Set the expression and immediately reduce to a number if trivial.

  if (maybe_expr) {
    auto* units = posting->mutable_spec()->mutable_units();
    SetExprOrNumber(units, *maybe_expr);
  }

  // Set the currency on the posting if present.
  if (maybe_currency.has_value()) {
    auto* units = posting->mutable_spec()->mutable_units();
    units->set_currency(maybe_currency.value());
  }

  // Store flag and account name.
  if (flag != '\0') {
    posting->set_flag(&flag, 1);
  }
  posting->set_account(account);
}

void SetLocationFromLocation(const location& loc, Location* output) {
  if (loc.begin.filename) {
    output->set_filename(*loc.begin.filename);
  }
  output->set_lineno(loc.begin.line);
  output->set_lineno_end(loc.end.line);
}

void Builder::AddError(std::string_view message, const location& loc) {
  auto* error = new Error();
  errors_.push_back(error);
  error->set_message(Capitalize(message));
  SetLocationFromLocation(loc, error->mutable_location());
}

void Builder::ValidateAccountNames() {
  auto acctypes = options_->account_types();
  SetDefaultAccountTypes(&acctypes);
  re2::RE2 account_re = BuildAccountRegexp(acctypes);
  for (const auto& item : accounts_) {
    if (!re2::RE2::FullMatch(item.first, account_re)) {
      AddError(StrFormat("Invalid account name: '%s'", item.first), item.second);
    }
  }
}

void Builder::Finalize(const location& loc) {
  // Validate the account names, issuing errors as a side-effect.
  ValidateAccountNames();

  // If the user left some tags unbalanced, issue an error.
  for (const auto& tag : active_tags_) {
    AddError(StrFormat("Unbalanced pushed tag: '%s'", tag), loc);
  }

  // If the user left some metadata unpopped, issue an error.
  for (const auto& [key, value_list] : active_meta_) {
    AddError(StrFormat("Unbalanced metadata key '%s' has leftover metadata", key), loc);
  }

        // # Weave the commas option in the DisplayContext itself, so it propagates
        // # everywhere it is used automatically.
        // self.dcontext.set_commas(self.options['render_commas'])

        // # Build and store the inferred DisplayContext instance.
        // self.options['dcontext'] = self.dcontext

        // # Also record the name of the processed file.
        // self.options['filename'] = filename

        // return sorted(self.entries, key=data.entry_sortkey)

}

std::unique_ptr<Ledger> Builder::MakeLedger() {
  auto ledger = std::make_unique<Ledger>();
  ledger->directives = std::move(directives_);
  ledger->errors = std::move(errors_);
  ledger->options = std::move(options_);
  ledger->info = std::move(info_);
  assert(ledger->options);
  assert(ledger->info);
  return ledger;
}

}  // namespace parser
}  // namespace beancount
