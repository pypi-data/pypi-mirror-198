// Copyright (C) 2020  Martin Blais
// License: "GNU GPLv2"

#include "beancount/ccore/account.h"

#include <algorithm>
#include <string>
#include <initializer_list>
#include <iostream>

#include "absl/strings/str_cat.h"
#include "absl/strings/str_format.h"
#include "absl/strings/str_join.h"
#include "absl/strings/str_split.h"
#include "re2/re2.h"

namespace beancount {
using std::string_view;
using std::string;
using std::vector;

const char* kSep = ":";

// Regular expression string that matches valid account name components.
// Categories are:
//   Lu: Uppercase letters.
//   L: All letters.
//   Nd: Decimal numbers.
const char* kAccountCompTypeRe = "[\\p{Lu}][\\p{L}\\p{Nd}\\-]*";
const char* kAccountCompNameRe = "[\\p{Lu}\\p{Nd}][\\p{L}\\p{Nd}\\-]*";

// Regular expression string that matches a valid account, not taking into
// account the account types.
re2::RE2 kAccountRE(absl::StrFormat("(?:%s)(?:%s%s)+",
                                    kAccountCompTypeRe, kSep, kAccountCompNameRe));

// TODO(blais): Remove this.
// A dummy object which stands for the account type. Values in custom directives
// use this to disambiguate between string objects and account names.
// TYPE = '<AccountDummy>'

re2::RE2 BuildAccountRegexp(const options::AccountTypes& acctypes) {
  const string names_re = absl::StrJoin({
      acctypes.assets(),
      acctypes.liabilities(),
      acctypes.equity(),
      acctypes.income(),
      acctypes.expenses()}, "|");
  return re2::RE2(absl::StrFormat("(?:%s)(?:%s%s)+",
                                  names_re, kSep, kAccountCompNameRe));
}

bool IsAccountValid(string_view account) {
  return re2::RE2::FullMatch(account, kAccountRE);
}

string JoinAccount(const vector<string_view>& il) {
  return absl::StrJoin(il, kSep);
}

vector<string> SplitAccount(string_view account) {
  return absl::StrSplit(account, kSep);
}

string ParentAccount(string_view account) {
  if (account.empty()) {
    return "";
  }
  auto components = SplitAccount(account);
  return absl::StrJoin(components.begin(), components.end()-1, kSep);
}

string LeafAccount(string_view account) {
  if (account.empty()) {
    return "";
  }
  auto startpos = account.rfind(kSep);
  if (startpos == string::npos){
    return string(account);
  }
  auto begin = account.data() + startpos + 1;
  return string(begin, account.end() - begin);
}

string AccountSansRoot(string_view account) {
  if (account.empty()) {
    return "";
  }
  vector<string_view> components = absl::StrSplit(account, kSep);
  auto iter = components.begin() + 1;
  return absl::StrJoin(iter, components.end(), kSep);
}

string_view AccountRoot(string_view account, int num_components) {
  size_t pos = 0;
  for (int c = 0; c < num_components; ++c) {
    pos = account.find(kSep, pos + 1);
    if (pos == string::npos) {
      return account;
    }
  }
  return account.substr(0, pos);
}

bool HasAccountComponent(string_view account, string_view component) {
  return re2::RE2::PartialMatch(account, absl::StrCat("(^|:)", component, "(:|$)"));
}

string CommonPrefix(const vector<string_view>& accounts) {
  if (accounts.empty()) {
    return string{};
  }
  const string_view& first_account = accounts.front();
  size_t pos = 0;
  size_t newpos = 0;
  bool done = false;
  while (pos != string::npos) {
    newpos = first_account.find(kSep, pos + 1);
    size_t count = (newpos != string::npos) ? newpos - pos : string::npos;
    string_view component = first_account.substr(pos, count);
    for (const auto& account : accounts) {
      size_t fpos = account.find(kSep, pos + 1);
      size_t count = (fpos != string::npos) ? fpos - pos : string::npos;
      if (account.substr(pos, count) != component) {
        done = true;
        break;
      }
    }
    if (done)
      break;
    pos = newpos;
  }
  return string(first_account.substr(0, pos));
}



// TODO(blais): Continue here.

// def walk(root_directory):
//     """A version of os.walk() which yields directories that are valid account names.
//
//     This only yields directories that are accounts... it skips the other ones.
//     For convenience, it also yields you the account's name.
//
//     Args:
//       root_directory: A string, the name of the root of the hierarchy to be walked.
//     Yields:
//       Tuples of (root, account-name, dirs, files), similar to os.walk().
//     """
//     for root, dirs, files in os.walk(root_directory):
//         dirs.sort()
//         files.sort()
//         relroot = root[len(root_directory)+1:]
//         account_name = relroot.replace(os.sep, sep)
//         if is_valid(account_name):
//             yield (root, account_name, dirs, files)
//
//
// def parent_matcher(account_name):
//     """Build a predicate that returns whether an account is under the given one.
//
//     Args:
//       account_name: The name of the parent account we want to check for.
//     Returns:
//       A callable, which, when called, will return true if the given account is a
//       child of ``account_name``.
//     """
//     return re.compile(r'{}($|{})'.format(re.escape(account_name), sep)).match
//
//
// def parents(account_name):
//     """A generator of the names of the parents of this account, including this account.
//
//     Args:
//       account_name: The name of the account we want to start iterating from.
//     Returns:
//       A generator of account name strings.
//     """
//     while account_name:
//         yield account_name
//         account_name = parent(account_name)
//
//
// class AccountTransformer:
//     """Account name transformer.
//
//     This is used to support Win... huh, filesystems and platforms which do not
//     support colon characters.
//
//     Attributes:
//       rsep: A character string, the new separator to use in link names.
//     """
//     def __init__(self, rsep=None):
//         self.rsep = rsep
//
//     def render(self, account_name):
//         "Convert the account name to a transformed account name."
//         return (account_name
//                 if self.rsep is None
//                 else account_name.replace(sep, self.rsep))
//
//     def parse(self, transformed_name):
//         "Convert the transform account name to an account name."
//         return (transformed_name
//                 if self.rsep is None
//                 else transformed_name.replace(self.rsep, sep))
//

}  // namespace beancount
