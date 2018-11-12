import urllib.request,json
from datetime import datetime
from .models import Source
from .models import Article

# Getting api key
api_key = None
# Getting the Category url
sources_url = None
# Getting the Headline url
Headline_url = None
#Getting the Everything url
Everything_url = None
#Search url
search_url = None



def configure_request(app):
    global api_key,Everything_url,Headline_url, sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    Headline_url = app.config['HEADLINE_BASE_URL']
    Article_url=app.config['EVERYTHING_BASE_URL']
    search_url = app.config["SEARCH_API_BASE_URL"]

def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        print(get_newsource_response)

        newsource_results = None

        if get_newsource_response['sources']:
            newsource_results_list = get_newsource_response['sources']
            newsource_results = process_results(newsource_results_list)

    return newsource_results


def process_results(newsource_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects
    Args:
        newsource_list: A list of dictionaries that contain news source details
    Returns :
        newsource_results: A list of newsource objects
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        name = news_item.get('title')
        title = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        newsource_object = Source(id,title,name,description,url)
        newsource_results.append(newsource_object)

    return newsource_results

