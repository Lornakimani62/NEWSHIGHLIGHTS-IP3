from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_newsource,get_articles
from ..models import Source,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('general')
    technology_newsource = get_newsource('technology')
    entertainment_newsource = get_newsource('entertainment')
    sports_newsource = get_newsource('sports')
    business_newsource = get_newsource('business')
    science_newsource = get_newsource('science')

    return render_template('index.html',general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View article page function returns the articles based on a new source
    '''

    #Getting articles
    article = get_articles(source_id)
    title = f'{source_id}'
    


    return render_template('article.html', title=title,articles=article)