import logging
import requests
import scrapy

from alexa import BASE_URL, helpers

URL = f"{BASE_URL}/topsites"


def get_sites(country_code=None):
    """Returns an ordered list of top websites from alexa.com.
    Args:
        country_code (string): two-letter code, ex. "US" (default global).
    Returns:
        list of strings, or None: top websites ordered by rank,
        (None if invalid country_code).
    """
    if country_code:
        if get_country_name(country_code):
            url = f"{URL}/countries/{country_code.upper()}"
        else:
            logging.warning(f"Invalid country code: {country_code}")
            return
    else:
        url = URL
    response = helpers.get_response(url)
    sel = scrapy.Selector(text=response.text)
    sites = sel.css("div.site-listing a::text").extract()
    top_sites = [site.lower() for site in sites]
    return top_sites


def get_country_dictionary():
    """Returns a dictionary of country_names and their country_codes."""
    url = f"{URL}/countries"
    response = helpers.get_response(url)
    sel = scrapy.Selector(text=response.text)
    country_names = sel.css("ul[class='countries span3'] a::text").extract()
    country_links = sel.css("ul[class='countries span3'] a::attr(href)").extract()
    country_codes = [link.split("/")[-1] for link in country_links]
    return dict(zip(country_names, country_codes))


def get_country_code(country_name):
    """Returns country_code for a given country_name (case insensitive).
    Args:
        country_name (string): ex. "United States"
    Returns:
        string, or None: two-letter code, ex. "US" (None if not found)
    """
    countries = {name.upper(): code for name, code in get_country_dictionary().items()}
    if country_name.upper() in countries:
        return countries[country_name.upper()]


def get_country_name(country_code):
    """Returns country_name for a given country_code (case insensitive).
    Args:
        country_code (string): two-letter code, ex. "US"
    Returns:
        string, or None: ex. "United States" (None if not found)
    """
    countries = get_country_dictionary()
    for country_name in countries:
        if countries[country_name].upper() == country_code.upper():
            return country_name
