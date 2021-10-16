from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
    organization = StringField("Organization")
    email = StringField('Email',validators=[DataRequired(), Email()])

    comment = StringField('Comment', validators=[DataRequired()])

    submit = SubmitField('Submit')
