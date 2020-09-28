#!/usr/bin/env python3

import logging
import unittest

from context import siteinfo

logging.basicConfig(level=logging.INFO)

INPUTS = {
    "good": "google.com",
    "unformatted": "htTPs://WWW.GoOgLe.COM",
    "bad": "https://www.badbadbadbadinput.com",
    "invalid": "invalidinput.invalidinput",
}

FUNCS = {
    "get_competitors": siteinfo.get_competitors,
    "get_similar_sites": siteinfo.get_similar_sites,
    "get_rank": siteinfo.get_rank,
    "get_user_time": siteinfo.get_user_time,
    "get_search_terms": siteinfo.get_search_terms,
    "get_industry_topics": siteinfo.get_industry_topics,
}


class TestGetCompetitors(unittest.TestCase):
    test = "get_competitors"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetSimilarSites(unittest.TestCase):
    test = "get_similar_sites"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetRank(unittest.TestCase):
    test = "get_rank"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(isinstance(output, int))

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(isinstance(output, int))

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetUserTime(unittest.TestCase):
    test = "get_user_time"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(isinstance(output, int))

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(isinstance(output, int))

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetSearchTerms(unittest.TestCase):
    test = "get_search_terms"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetIndustryTopics(unittest.TestCase):
    test = "get_industry_topics"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


if __name__ == "__main__":
    unittest.main()
