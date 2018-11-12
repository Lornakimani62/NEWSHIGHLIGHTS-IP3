from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_newsource

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

    return render_template('index.html',general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource)