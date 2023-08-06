// Tests on exact serialization of Decimal.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>

#include "gtest/gtest.h"
#include "decimal.hh"
#include "mpdecimal.h"

#include "beancount/ccore/number.pb.h"
#include "beancount/ccore/number.h"

namespace {
using std::cout;
using std::endl;

TEST(SerializationTest, PrintComponents) {
  decimal::Decimal a("42e8");

  const mpd_t* value = a.getconst();
  cout << "sizeof(mpd_ssize_t) " << sizeof(mpd_ssize_t) << endl;
  cout << "sizeof(mpd_uint_t) " << sizeof(mpd_uint_t) << endl;

  cout << endl;

  cout << "flags " << value->flags << endl;
  cout << "exp " << value->exp << endl;
  cout << "digits " << value->digits << endl;
  cout << "len " << value->len << endl;
  cout << "alloc " << value->alloc << endl;
  cout << "exponent " << a.exponent() << endl;
  for (int ii = 0; ii < value->alloc; ++ii) {
    cout << "data[" << ii << "] " << value->data[ii] << endl;
  }
}

TEST(SerializationTest, RoundTripText) {
  decimal::Decimal a("42e8");

  // Serialize.
  beancount::Number number;
  number.set_exact(a.to_sci(false));
  cout << "'" << number.exact() << "'" << endl;

  // Deserialize.
  decimal::Decimal b(number.exact());

  EXPECT_EQ(b, a);
}

TEST(SerializationTest, RoundTripMpdTriple) {
  decimal::Decimal a("42e8");
  cout << "A = " << a << endl;

  // Serialize & deserialize via text.
  auto pb = beancount::DecimalToProto(a, beancount::CONV_TRIPLE);
  ASSERT_TRUE(pb.ok());
  auto b = beancount::ProtoToDecimal(*pb);
  ASSERT_TRUE(b.ok());
  cout << "B = " << *b << endl;

  // Serialize & deserialize via triple.
  auto pc = beancount::DecimalToProto(a, beancount::CONV_STRING);
  ASSERT_TRUE(pc.ok());
  auto c = beancount::ProtoToDecimal(*pc);;
  ASSERT_TRUE(c.ok());
  cout << "C = " << *c << endl;

  EXPECT_EQ(*b, a);
}

}  // namespace
