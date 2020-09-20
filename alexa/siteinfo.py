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
        list (string), or None: competitor websites
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    sites = eval(sel.css("script#competitorsJSON::text").extract_first())
    return sites.get("competitors")


def get_similar_sites(website):
    """Returns a list of similar sites for a given website.
    Args:
        website (string): example - "mysite.com"
    Returns:
        dict (string: float): similar websites and corresponding overlap score
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    sites = sel.css(
        "div#card_mini_audience div.Body > div.Row > div.site > a::text"
    ).extract()
    overlaps = sel.css(
        "div#card_mini_audience div.Body > div.Row > div.overlap > span.truncation::text"
    ).extract()
    similar_sites = {site.strip(): overlap for site, overlap in zip(sites, overlaps)}
    return similar_sites


def get_rank(website):
    """Returns alexa rank of given website.
    Args:
        website (string): example - "mysite.com"
    Returns:
        int: alexa rank
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    rank = int(
        sel.css(
            "div#card_mini_trafficMetrics div.rankmini-global > div.rankmini-rank::text"
        ).extract()[-1]
    )
    return rank


def _get_siteinfo(website):
    """Returns response object after properly formatting website string."""
    formatted = helpers.format_website_string(website)
    url = f"{URL}/{formatted}"
    return helpers.get_response(url)
