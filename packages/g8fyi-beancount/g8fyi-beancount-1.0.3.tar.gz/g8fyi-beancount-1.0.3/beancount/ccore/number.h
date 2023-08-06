// Copyright (C) 2020  Martin Blais
// License: "GNU GPLv2"

#ifndef BEANCOUNT_CCORE_NUMBER_H_
#define BEANCOUNT_CCORE_NUMBER_H_

#include <string>
#include <iosfwd>

#include "beancount/ccore/number.pb.h"

#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "decimal.hh"


namespace std {

// Hashing function for Decimal type.
//
// Note: This is not provided by the mpdecimal library, but has an
// implementation in Python's _decimal.c wrappers.
template<>
struct hash<beancount::MpdTriple> {
  size_t operator()(const beancount::MpdTriple& tp) const {
    return (hash<uint32_t>{}(tp.tag()) ^
            hash<uint32_t>{}(tp.sign()) ^
            hash<uint64_t>{}(tp.hi()) ^
            hash<uint64_t>{}(tp.lo()) ^
            hash<int64_t>{}(tp.exp()));
  }
};

template<>
struct hash<beancount::Number> {
  size_t operator()(const beancount::Number& number) const {
    return (number.has_exact() ?
            hash<std::string>{}(number.exact()) :
            hash<beancount::MpdTriple>{}(number.triple()));
  }
};

}  // namespace std

namespace beancount {

// A type for the particular conversion requested.
enum DecimalConversion {
  CONV_STRING = 10,
  CONV_MPD = 11,
  CONV_TRIPLE = 12,
};

// Deserialize a Number proto to a mpdecimal number.
absl::StatusOr<decimal::Decimal> ProtoToDecimal(const Number& proto);
decimal::Decimal ProtoToDecimalOrDie(const Number& proto);

// Serialize a mpdecimal number to a Number proto.
absl::StatusOr<Number> DecimalToProto(const decimal::Decimal& dec,
                                      DecimalConversion conversion);
absl::Status DecimalToProto(const decimal::Decimal& dec,
                            DecimalConversion conversion,
                            Number* proto);

// Comparison operators for decimal protos.
bool operator==(const Number& proto1, const Number& proto2);

// Streaming operator for Number proto.
std::ostream& operator<<(std::ostream& os, const Number& proto);

// Copy `src` to `buffer` stripping commas on the way, for a fixed number of
// characters.
void CopySansCommas(const char* src, char* buffer, size_t num_chars);

}  // namespace beancount

#endif // BEANCOUNT_CCORE_NUMBER_H_
