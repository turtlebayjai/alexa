#!/usr/bin/env python3

import logging
import unittest

from context import siteinfo

logging.basicConfig(level=logging.INFO)


class TestGetCompetitors(unittest.TestCase):
    def test_nice_input(self):
        website = "google.com"
        competitors = siteinfo.get_competitors(website)
        self.assertTrue(len(competitors) > 0)

    def test_unformatted_input(self):
        website = "htTPs://WWW.GoOgLe.COM"
        competitors = siteinfo.get_competitors(website)
        self.assertTrue(len(competitors) > 0)

    def test_invalid_website(self):
        website = "https://www.badinput.com"
        competitors = siteinfo.get_competitors(website)
        self.assertEqual(competitors, None)

    def test_invalid_input(self):
        website = "https://www.badinput.badinput"
        competitors = siteinfo.get_competitors(website)
        self.assertEqual(competitors, None)


class TestGetSimilarSites(unittest.TestCase):
    def test_nice_input(self):
        website = "google.com"
        similar = siteinfo.get_similar_sites(website)
        self.assertTrue(len(similar) > 0)

    def test_unformatted_input(self):
        website = "htTPs://WWW.GoOgLe.COM"
        similar = siteinfo.get_similar_sites(website)
        self.assertTrue(len(similar) > 0)

    def test_invalid_website(self):
        website = "https://www.badinput.com"
        similar = siteinfo.get_similar_sites(website)
        self.assertEqual(similar, None)

    def test_invalid_input(self):
        website = "https://www.badinput.badinput"
        similar = siteinfo.get_similar_sites(website)
        self.assertEqual(similar, None)


if __name__ == "__main__":
    unittest.main()
