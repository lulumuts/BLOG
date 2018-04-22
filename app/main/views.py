from flask import Flask, render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts,Comments,Subscription
from ..import db
from .forms import PostsForm,CommentsForm,SubscriptionForm
import markdown2
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin


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

@main.route('/posts/<int:id>',methods = ["GET","POST"])
def single_post(id):

    post=Posts.query.get(id)
    comment=Comments.query.filter_by(posts_id=id).all()


    form= CommentsForm()
    # comment=Comments.query.filter_by(posts_id=id).all()

    if form.validate_on_submit():
        comment = form.comment.data

        # updated review instance
        new_comment = Comments(comment = comment,posts_id = id)

        #save review method
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.single_post',id = post.id))



    format_post = markdown2.markdown(post.content,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('new_post.html',format_post=format_post,comments_form=form,comment=comment, post=post)

@main.route('/comments', methods = ['GET','POST'])
@login_required
def new_comment():

    form= CommentsForm()
    # comment=Comments.query.filter_by(posts_id=id).all()

    if form.validate_on_submit():
        comment = form.comment.data

        # updated review instance
        new_comment = Comments(comment = comment)

        #save review method
        new_comment.save_comment()
        return redirect(url_for('.index'))


    return render_template('comments.html', comments_form=form )

@main.route('/subscription',methods = ["GET","POST"])
def subscriber():

    form= SubscriptionForm()


    if form.validate_on_submit():
        email = form.email.data
        date = form.date.data


        # updated review instance
        new_subscriber = Subscription(email=email,date = date,user_id=current_user.id)

        #save review method
        new_subscriber.save_subscriber()
        return redirect(url_for('subscriber'))


    return render_template('index.html',title= title, subscribe_form=form )
