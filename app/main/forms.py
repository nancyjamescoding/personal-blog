from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired


class BlogForm(FlaskForm):
    title = StringField('blog_title')
    text = TextAreaField('blog_text')
    category = SelectField('blog_type', choices=[(
        'technology', 'Product-Pitch'), ('travels', 'Interview-Pitch'), ('sports', 'Promotion-Pitch')])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    text = TextAreaField('yoursay')
    submit = SubmitField('submit')
