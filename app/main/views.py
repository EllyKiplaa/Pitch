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

@main.route('/categories/new-pitch/add/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
                                              
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        pitch = form.pitch.data
        title = form.title.data
        new_pitch= Pitch( title=title, pitch=pitch, user_id=current_user.id)
        new_pitch.save_pitch() 
        return redirect(url_for('.category', id=category.id))


    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form, category=category)

@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    ''' 
    function to post comments 
    '''
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

    comment = Comments.get_comments(id)
    return render_template('pitch.html', pitches=pitches, comment=comment, category_id=id)

