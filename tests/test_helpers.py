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


if __name__ == "__main__":
    unittest.main()
