#!/usr/bin/env python3

import logging
import unittest

from context import topsites

logging.basicConfig(level=logging.INFO)


class TestGetSites(unittest.TestCase):
    def test_global_list(self):
        global_list = topsites.get_sites()
        self.assertTrue(len(global_list) > 0)
        self.assertTrue("google.com" in global_list)

    def test_valid_codes(self):
        us_list = topsites.get_sites("US")
        self.assertTrue(len(us_list) > 0)
        self.assertTrue("google.com" in us_list)
        us_list = topsites.get_sites("uS")
        self.assertTrue(len(us_list) > 0)
        self.assertTrue("google.com" in us_list)

    def test_invalid_codes(self):
        no_list = topsites.get_sites("NONE")
        self.assertEqual(no_list, None)


class TestGetCountryDictionary(unittest.TestCase):
    def test_dictionary(self):
        countries = topsites.get_country_dictionary()
        self.assertTrue(len(countries) > 0)
        self.assertEqual(countries["United States"], "US")


class TestGetCountryCode(unittest.TestCase):
    def test_valid_codes(self):
        self.assertEqual(topsites.get_country_code("United States"), "US")
        self.assertEqual(topsites.get_country_code("uniTed sTaTes"), "US")

    def test_invalid_codes(self):
        self.assertEqual(topsites.get_country_code("none_country"), None)


class TestGetCountryName(unittest.TestCase):
    def test_valid_names(self):
        self.assertEqual(topsites.get_country_name("US"), "United States")
        self.assertEqual(topsites.get_country_name("us"), "United States")

    def test_invalid_codes(self):
        self.assertEqual(topsites.get_country_code("none"), None)


if __name__ == "__main__":
    unittest.main()
