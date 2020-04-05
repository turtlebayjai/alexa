import requests

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
        url = "%s/countries/%s" % (_BASE_URL, country_code)
    else:
        url = _BASE_URL
    print("Requesting from %s ..." % url)
    try:
        response = requests.get(url, headers=headers, timeout=5.0)
    except requests.exceptions.ReadTimeout:
        raise ValueError(
            "Request timed out. Possible invalid country code: %s" % country_code)

    top_sites = []
    if response.status_code == 200:
        html_body = response.text
        div_start = html_body.find('<div class="tr site-listing">', 0)
        while div_start != -1:
            link = _extract_link_from_div(html_body, div_start)
            if link:
                top_sites.append(link)
            div_start = html_body.find(
                '<div class="tr site-listing">', div_start + 1)
    else:
        raise ValueError(
            "Something went wrong. HTTP status code: %d" % response.status_code)
    return top_sites


def _extract_link_from_div(text, div_start):
    element_start = text.find('<a href=', div_start)
    site_start = text.find('>', element_start) + 1
    site_end = text.find('</a>', element_start)
    if element_start == -1 or site_end == -1 or site_start > site_end:
        site = None
    else:
        site = text[site_start:site_end].lower()
    return site
