from flask import Flask, render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts
from ..import db
from .forms import PostsForm
import markdown2

@main.route('/')
def index():

    title = 'Start your blog journey here'

    return render_template('index.html', title=title)

@main.route('/posts', methods = ['GET','POST'])
@login_required
def new_post():

    form= PostsForm()


    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data


        # updated review instance
        new_post = Posts(title=title,content = content,user_id=current_user.id)

        #save review method
        new_post.save_post()
        return redirect(url_for('.index'))

    title = f'{Posts.title}'
    return render_template('posts.html',title= title, posts_form=form )

@main.route('/posts/<int:id>')
def single_post(id):
    post=Post.query.get(id)
    if post is None:
        abort(404)
    format_post = markdown2.markdown(post.content,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('new-posts.html',content = content,format_post=format_post)
