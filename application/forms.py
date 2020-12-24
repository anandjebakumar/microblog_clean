from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from .models import User

class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired()
        ]
    )
    remember_me = BooleanField(label='Remember me')
    submit = SubmitField(label='Sign in')

class RegistrationForm(FlaskForm):
    username = StringField(
        label = 'Username',
        validators=[
            DataRequired()
        ]
    )
    email = StringField(
        label = 'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        label = 'Password',
        validators=[
            DataRequired()
        ]
    )
    repeat_password = PasswordField(
        label = 'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField(
        label='Register'
    )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.') 

class EditProfileForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[
            DataRequired()
        ]
    )
    about_me = TextAreaField(
        label='About me',
        validators=[
            Length(min=0, max=140)
        ]
    )
    submit = SubmitField('Submit')