from flask import Flask, render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User
from ..import db

@main.route('/')
def index():

    title = 'Start your blog journey here'

    return render_template('index.html', title=title)
