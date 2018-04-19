from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PostsForm(FlaskForm):

    title = StringField('Blog title', validators=[Required()])
    content = TextAreaField('Blog post', validators=[Required()])
    submit = SubmitField('Submit')
