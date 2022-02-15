from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

   blog = StringField('blog',validators=[Required()])
   comment = TextAreaField('comment', validators=[Required()])
   submit = SubmitField('Submit')
