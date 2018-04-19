from flask import Flask, render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts,Comments
from ..import db
from .forms import PostsForm,CommentsForm
import markdown2

@main.route('/')
def index():
    form= PostsForm()


    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data


    title = 'Start your blog journey here'
    post=Posts.query.all()

    return render_template('index.html', title=title,post = post)

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

    post=Posts.query.get(id)
    comment=Comments.query.filter_by(posts_id=id).all()

    format_post = markdown2.markdown(post.content,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('new_post.html',format_post=format_post,comment=comment)

@main.route('/comments', methods = ['GET','POST'])
@login_required
def new_comment():

    form= CommentsForm()

    if form.validate_on_submit():
        comment = form.comment.data

        # updated review instance
        new_comment = Comments(comment = comment)

        #save review method
        new_comment.save_comment()
        return redirect(url_for('.index'))


    return render_template('comments.html', comments_form=form )


# @main.route('/comments/<int:id>')
# def single_comment(id):
#     comment=Comments.query.get(id)
#
#     format_post = markdown2.markdown(post.content,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('new_post.html',format_post=format_post)
