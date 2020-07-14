from flask import render_template,redirect,url_for
from . import main
from ..models import User



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    User = User.get_category()

    title = 'Pitch your idea for you a so brilliant'

    return render_template('index.html', category = User)

