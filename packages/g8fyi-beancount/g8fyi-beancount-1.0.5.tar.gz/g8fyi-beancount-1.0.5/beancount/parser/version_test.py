__copyright__ = "Copyright (C) 2018  Martin Blais"
__license__ = "GNU GPLv2"

import unittest

import g8fyi_beancount
from g8fyi_beancount.parser import version


class TestVersion(unittest.TestCase):

    def test_version_exists(self):
        self.assertRegex(getattr(g8fyi_beancount, "__version__", ""), r"\d+\.\d+\.\d+")

    def test_compute_version_string(self):
        self.assertEqual(
            'Beancount 2.1.0 (hg:e291c91b37e1; 2018-05-12)',
            version.compute_version_string(
                '2.1.0', 'hg:e291c91b37e1d21c29645d93473a7917bb726699', 1526099371))

        self.assertEqual(
            'Beancount 2.1.0 (git:e291c91b; 2018-05-12)',
            version.compute_version_string(
                '2.1.0', 'git:e291c91b37e1d21c29645d93473', 1526099371))

        self.assertEqual(
            'Beancount 2.1.0',
            version.compute_version_string(
                '2.1.0', '', 0))


if __name__ == '__main__':
    unittest.main()
