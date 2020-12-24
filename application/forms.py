from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
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