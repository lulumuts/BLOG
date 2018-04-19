from flask import Flask, render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts
from ..import db

@main.route('/')
def index():

    title = 'Start your blog journey here'

    return render_template('index.html', title=title)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form= ReviewForm()
#
#     movie= get_movie(id)
#
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#
#         # updated review instance
#         new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)
#
#         #save review method
#         new_review.save_review()
#         return redirect(url_for('.movie',id = movie.id ))
#
#     title = f'{movie.title} review'
#     return render_template('new_review.html',title= title, review_form=form, movie=movie)
