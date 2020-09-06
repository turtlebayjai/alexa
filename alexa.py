import logging
import requests
import scrapy

_BASE_URL = "https://www.alexa.com/topsites"


def get_url(country_code=None):
    """Returns the URL of top websites from alexa.com.
    Args:
        country_code(string): two-letter code, ex. "US" (default global).
    Returns:
        string: URL
    """
    response = _get_response(country_code)
    return response.url


def get_top_sites(country_code=None, headers=None):
    """Returns an ordered list of top 50 websites from alexa.com.
    Args:
        country_code (string): two-letter code, ex. "US" (default global).
        headers (dict): optional headers for HTTP request (default None).
    Returns:
        list of strings: the top 50 websites ordered by rank.
    """
    response = _get_response(country_code=country_code, headers=headers)
    sel = scrapy.Selector(text=response.text)
    sites = sel.css("div.site-listing a::text").extract()
    top_sites = [site.lower() for site in sites]
    return top_sites


def _get_response(country_code=None, headers=None):
    """Returns response object and does error checking."""
    if country_code:
        url = f"{_BASE_URL}/countries/{country_code}"
    else:
        url = _BASE_URL

    logging.info(f"Requesting from {url} ...")
    try:
        response = requests.get(url, headers=headers, timeout=5.0)
    except requests.exceptions.ReadTimeout as e:
        raise requests.exceptions.ReadTimeout(
            f"Request timed out. Possible invalid country code: {country_code}"
        )
    else:
        if response.status_code != 200:
            raise ValueError(
                f"Something went wrong. HTTP status code: {response.status_code}"
            )
    return response
