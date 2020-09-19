#!/usr/bin/env python3

import logging
import unittest

from context import helpers

logging.basicConfig(level=logging.INFO)


class TestGetResponse(unittest.TestCase):
    def test_valid_url(self):
        url = "https://www.alexa.com/topsites"
        response = helpers.get_response(url)
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        url = "https://www.alexa.com/invalidinvalid"
        with self.assertRaises(ValueError):
            helpers.get_response(url)


class TestFormatWebsite(unittest.TestCase):
    def test_lower(self):
        website = "GOOGLE.COM"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")

    def test_prefixes(self):
        website = "https://google.com"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")
        website = "http://google.com"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")
        website = "www.google.com"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")

    def test_combined(self):
        website = "htTPs://WWW.GoOgLe.COM"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")
        website = "htTP://WWW.GoOgLe.COM"
        formatted = helpers.format_website_string(website)
        self.assertEqual(formatted, "google.com")


if __name__ == "__main__":
    unittest.main()
