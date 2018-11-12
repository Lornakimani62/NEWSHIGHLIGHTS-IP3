from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_newsource
from ..models import Source

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('sources')
    

    return render_template('index.html',general = general_newsource)