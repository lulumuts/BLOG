from flask import Flask, render_template
from . import main

@main.route('/')
def index():

    title = 'Start your blog journey here'

    return render_template('index.html', title=title)
