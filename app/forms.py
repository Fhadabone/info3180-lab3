from flask_wtf import FlaskForm
from wtforms.fields import TextField
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    fullname = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])
    submit = SubmitField('Send')
