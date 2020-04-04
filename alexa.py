import requests

BASE_URL="https://www.alexa.com/topsites"

"""
Structure of a top site entry:

                <div class="tr site-listing">
                  <div class="td">3</div>     
                  <div class="td DescriptionCell">
                    <p class="">
                        <a href="/siteinfo/tmall.com">Tmall.com</a>                
                    </p>
                  </div>
                   <div class="td right"><p>6:44</p></div>
                   <div class="td right"><p>2.88</p></div>
                   <div class="td right"><p>0.90%</p></div>
                   <div class="td right"><p>4,592</p></div>
                </div>
"""


def get_top_sites(country_code=None):
    """ 
    Returns a list of top 50 websites from alexa.com 
  
    Parameters: 
    country_code (string): Optional two-letter code, ex. "US". Defaults to global results.

    Returns: 
    list of strings: Top 50 websites, ordered by rank. 
                     Websites are NOT prefixed with 'https://www.' 
    """

    if country_code:
        URL = BASE_URL+"/countries/"+country_code
    else:
        URL = BASE_URL

    print("Requesting from", URL, "...") 
    response = requests.get(URL, timeout=3.0)

    if response.status_code == 200:
        top_sites = []
        html_body = response.text
        div_start = html_body.find('<div class="tr site-listing">', 0)
        while div_start != -1:
            link = _extract_link_from_div(html_body, div_start)
            if link:
                top_sites.append(link)
            div_start = html_body.find('<div class="tr site-listing">', div_start + 1)
        return top_sites
    else:
        error_message = "Something went wrong. HTTP status code: " + str(response.status_code)
        raise ValueError(error_message)


def _extract_link_from_div(text, div_start):
    element_start = text.find('<a href=', div_start)
    site_start = text.find('>', element_start) + 1
    site_end = text.find('</a>', element_start)
    if element_start == -1 or site_end == -1 or site_start > site_end:
        site = None
    else:
        site = text[site_start:site_end].lower()
    return site

