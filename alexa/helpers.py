import logging
import requests


def get_response(url, headers=None, params=None, timeout=5.0):
    """Returns a URL response if HTTP status 200."""
    logging.info(f"Requesting from {url} ...")
    response = requests.get(url, headers=None, params=None, timeout=timeout)
    if response.status_code != 200:
        raise ValueError(
            f"Something went wrong. HTTP status code: {response.status_code}"
        )
    return response


def format_website_string(website):
    """Returns a formatted website string to be used for siteinfo.
    Args:
        website (string): user-supplied.
    Returns:
        string: lower-case, prefixes removed.
    """
    formatted = website.lower()
    prefixes = ["https://", "http://", "www."]
    for prefix in prefixes:
        if formatted.startswith(prefix):
            formatted = formatted[len(prefix) :]
    return formatted
