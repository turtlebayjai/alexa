import requests
import scrapy

_BASE_URL = "https://www.alexa.com/topsites"


def get_top_sites(country_code=None, headers=None):
    """Returns a list of top 50 websites from alexa.com.
    Args:
        country_code (string): two-letter code, ex. "US" (default global).
        headers (dict): optional headers for HTTP request (default None).
    Returns:
        list of strings: the top 50 websites ordered by rank.
    Raises:
        ValueError: timeout, invalid country_code, HTTP status not 200.
    """
    if country_code:
        url = f"{_BASE_URL}/countries/{country_code}"
    else:
        url = _BASE_URL

    print(f"Requesting from {url} ...")
    try:
        response = requests.get(url, headers=headers, timeout=5.0)
    except requests.exceptions.ReadTimeout:
        raise ValueError(
            f"Request timed out. Possible invalid country code: {country_code}")
    else:
        if response.status_code != 200:
            raise ValueError(
                f"Something went wrong. HTTP status code: {response.status_code}")

    sel = scrapy.Selector(text=response.text)
    sites = sel.css("div.site-listing a::text").extract()
    top_sites = [site.lower() for site in sites]
    return top_sites
