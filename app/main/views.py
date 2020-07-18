from flask import render_template,redirect,url_for,abort    
from . import main
from ..models import User,Category,Comment,Pitch
from flask_login import login_required



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    category = Category.get_categories()
    title = 'Pitch your idea for you a so brilliant'

    return render_template('index.html', category = category)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

