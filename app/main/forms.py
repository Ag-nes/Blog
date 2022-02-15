from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import input_required


class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [input_required()])
    submit = SubmitField('Update')


class UpdatePost(FlaskForm):
    text = TextAreaField('Edit post here',validators = [input_required()])
    submit = SubmitField('Update')


class PostForm(FlaskForm):
    post_text = TextAreaField('Your post here', validators=[input_required()]) 
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    post_comment = TextAreaField('Make a comment', validators=[input_required()])
    submit = SubmitField('Comment')