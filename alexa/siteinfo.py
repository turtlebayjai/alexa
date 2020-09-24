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
        list (string): competitor websites
        (Returns None if website not found)
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    extracted = sel.css("script#competitorsJSON::text").extract_first()
    competitors = None
    if extracted:
        competitors = eval(extracted).get("competitors")
    return competitors or None


def get_similar_sites(website):
    """Returns a list of similar sites for a given website.
    Args:
        website (string): example - "mysite.com"
    Returns:
        dict (string: float): similar websites and corresponding overlap score
        (Returns None if website not found)
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    sites = sel.css(
        "div#card_mini_audience div.Body > div.Row > div.site > a::text"
    ).extract()
    overlaps = sel.css(
        "div#card_mini_audience div.Body > div.Row > div.overlap > span.truncation::text"
    ).extract()
    similar_sites = None
    if sites and overlaps:
        similar_sites = {
            site.strip(): overlap for site, overlap in zip(sites, overlaps)
        }
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
    extracted = sel.css(
        "div#card_mini_trafficMetrics div.rankmini-global > div.rankmini-rank::text"
    ).extract()
    rank = None
    if extracted:
        rank = int(extracted[-1])
    return rank


def get_user_time(website):
    """Returns average time in seconds that a visitor spends on the
        given website each day.
    Args:
        website (string): example - "mysite.com"
    Returns:
        int: seconds
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    extracted = sel.css(
        "div#card_mini_trafficMetrics div.rankmini-daily > div.rankmini-rank::text"
    ).extract_first()
    time = None
    if extracted:
        mins, secs = extracted.strip().split(":")
        time = int(mins) * 60 + int(secs)
    return time


def get_top_search_terms(website):
    """Returns top search terms driving traffic to the website,
        with corresponding percentage of search traffic from the term.
    Args:
        website (string): example - "mysite.com"
    Returns:
        dict (string: float): top search terms and corresponding percentages
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    terms = sel.css(
        "div#card_mini_topkw div.Body > div.Row > div.keyword > span.truncation::text"
    ).extract()
    percentages = sel.css(
        "div#card_mini_topkw div.Body > div.Row > div.metric_one > span.truncation::text"
    ).extract()
    top_terms = {
        term: float(percent.strip("%")) / 100
        for term, percent in zip(terms, percentages)
    }
    return top_terms


def get_top_industry_topics(website):
    """Returns top industry topics that this website or competitors
        published articles on.
    Args:
        website (string): example - "mysite.com"
    Returns:
        list (string): top industry topics
    """
    response = _get_siteinfo(website)
    sel = scrapy.Selector(text=response.text)
    topics = sel.css(
        "div#card_mini_topics div.TopicList > div.Showme > span::text"
    ).extract()
    return topics


def _get_siteinfo(website):
    """Returns response object after properly formatting website string."""
    formatted = helpers.format_website_string(website)
    url = f"{URL}/{formatted}"
    return helpers.get_response(url)
