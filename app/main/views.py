from flask import render_template,redirect,url_for
from . import main
from ..models import User
from flask_login import login_required



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    User = User.get_category()

    title = 'Pitch your idea for you a so brilliant'

    return render_template('index.html')

@main.route('/pitch/new',methods=["GET","POST"])
def new_pitch():
    
    form = "form"
    title = ''
    pitches=""

    return render_template('pitch.html', title=title, form=form, pitch_list=pitches)

@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment():

    comment_form="comment_form"
    comments = ''
    return render_template('form.html', comment_form=comment_form, comment_list=comments)


