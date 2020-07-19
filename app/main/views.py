from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User, Pitch, Category, Comment
from flask_login import login_required, current_user
from .forms import  PitchForm, CommentForm, CategoryForm
from .. import db

#Views
@main.route('/')
def index():
  
   
    category = Category.get_categories()


    return render_template('index.html',  category = category)

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():

    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))

    
    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title)


@main.route('/categories/<int:id>')
def category(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)

    return render_template('category.html', category=category)

@main.route('/categories/view_pitch/add/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
                                              
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch= Pitch(content=content,category= category.id,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('view_pitch.html', id=category.id))


    title = 'New Pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    ''' function to post comments '''
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion=opinion, user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', id=pitches.id))

    return render_template('post_comment.html', comment_form=form, title=title)

@main.route('/categories/view_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
 

    print(id)
    pitches = Pitch.query.get(id)
   

    if pitches is None:
        abort(404)
    #
    comment = Comments.get_comments(id)
    return render_template('pitch.html', pitches=pitches, comment=comment, category_id=id)

#Routes upvoting/downvoting pitches
@main.route('/pitch/upvote/<int:id>')
@login_required
def upvote(id):
    '''
    View function that add one to the vote_number column in the votes table
    '''
    pitch_id = Pitch.query.filter_by(id=id).first()

    if pitch_id is None:
         abort(404)

    new_vote = Votes(vote=int(1), user_id=current_user.id, pitches_id=pitch_id.id)
    new_vote.save_vote()
    return redirect(url_for('.view_pitch', id=id))

@main.route('/pitch/downvote/<int:id>')
@login_required
def downvote(id):

    '''
    View function that add one to the vote_number column in the votes table
    '''
    pitch_id = Pitch.query.filter_by(id=id).first()

    if pitch_id is None:
         abort(404)

    new_vote = Votes(vote=int(2), user_id=current_user.id, pitches_id=pitch_id.id)
    new_vote.save_vote()
    return redirect(url_for('.view_pitch', id=id))

@main.route('/pitch/downvote/<int:id>')
def vote_count(id):
    '''
    View function to return the total vote count per pitch
    '''
    votes = Votes.query.filter_by(user_id=user_id, line_id=line_id).all()

    total_votes = votes.count()

    return total_votes

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



