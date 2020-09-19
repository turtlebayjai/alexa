import json
import logging
import requests
import scrapy

from alexa import BASE_URL, helpers

URL = f"{BASE_URL}/siteinfo"


def get_competitors(website):
    """Returns a list of competitors for a given website.
    Args:
        website (string): example - "mysite.com"
    Returns:
        list of strings, or None: competitor websites.
    """
    formatted = helpers.format_website_input(website)
    url = f"{URL}/{formatted}"
    response = helpers.get_response(url)
    sel = scrapy.Selector(text=response.text)
    sites = eval(sel.css("script#competitorsJSON::text").extract_first())
    return sites.get("competitors")
