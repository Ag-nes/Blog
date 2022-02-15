from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField ,ValidationError
from wtforms.validators import input_required, Email, EqualTo
from ..models import User


class SignupForm(FlaskForm):
    username = StringField('Enter your name', validators=[input_required()])
    email = StringField('Enter your email address', validators=[input_required(),Email()])
    password = PasswordField('Password',validators = [input_required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [input_required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('A user with that email address exists')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('THis username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[input_required(),Email()])
    password = PasswordField('Password',validators =[input_required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    