from flask import render_template,redirect,url_for
from app import main
from ..models import Category   



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = "Hello world "
    return render_template('index.html', message = message)