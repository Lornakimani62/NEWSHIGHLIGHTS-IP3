import os

class Config:
    '''
    General configuration parent class
    '''

    HEADLINE_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    EVERYTHING_BASE_URL='https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news&sortBy=publishedAt&pageSize={}apiKey={}'
    SEARCH_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}