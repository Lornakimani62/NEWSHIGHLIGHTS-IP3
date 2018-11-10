import os

class Config:
    '''
    General configuration parent class
    '''

    HEADLINE_BASE_URL='https://newsapi.org/v2/top-headlines?sources=bbc-news&language=en&apiKey=a3bd9e0f12ad45a79350ccc74aeee6eb'
    EVERYTHING_BASE_URL='https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news&apiKey=a3bd9e0f12ad45a79350ccc74aeee6eb'
    NEWS_API_KEY = os.environ.get('a3bd9e0f12ad45a79350ccc74aeee6eb')
    SECRET_KEY = os.environ.get('0722212432')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}