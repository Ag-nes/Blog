from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User, Pitches, Comments
from flask_login import login_required, current_user
from .forms import EditProfile, PitchForm, CommentForm, UpdatePost
from .. import db, photos
from ..requests import get_quote
from sqlalchemy import desc
from ..email import mail_message


@main.route('/')
def home():
    quote = get_quote()

    pitches=Pitches.query.all()
    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    recent_post = Pitches.query.order_by(desc(Pitches.id)).all()

    return render_template('pitches.html', quote=quote, pitches=pitches, posted_by=posted_by, user=user, recent_post=recent_post)


@main.route('/new_pitch', methods=['GET','POST'])
@login_required
def pitch_form():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        text = pitch_form.pitch_text.data
        new_pitch = Pitches(text=text, user=current_user)
        new_pitch.save_pitch()

        data = User.query.all()
        for user in data:
            mail_message('New post up!', 'email/new_post', user.email, user=user)
            return redirect(url_for('main.home'))
    return render_template('new_pitch.html', pitch_form=pitch_form, )


@main.route('/edit_post/<int:pitch_id>', methods=['GET','POST'])
@login_required
def update_post(pitch_id):
    pitch = Pitches.query.filter_by(id=pitch_id).first()

    form = UpdatePost()
    if form.validate_on_submit():
        pitch.text=form.text.data
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('.home', pitch_id=pitch.id))
    return render_template('edit_post.html', form=form)


@main.route('/delete_post/<int:pitch_id>', methods=['GET','POST'])
@login_required
def delete_post(pitch_id):
    pitch = Pitches.query.filter_by(id=pitch_id).first()

    db.session.delete(pitch)
    db.session.commit()
    return redirect(url_for('.home', pitch_id=pitch.id))


@main.route('/comments/<int:pitch_id>', methods=['GET','POST'])
def pitch_comments(pitch_id):
    comments = Comments.get_comments(pitch_id)

    pitch = Pitches.query.get(pitch_id)
    pitch_posted_by = pitch.user_id
    user = User.query.filter_by(id=pitch_posted_by).first()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.pitch_comment.data      
        new_comment = Comments(comment=comment, pitch_id=pitch_id, user_id=current_user.get_id())
        new_comment.save_comment()
        return redirect(url_for('main.pitch_comments',pitch_id = pitch_id))

    return render_template('comments.html', comment_form=form, comments=comments, pitch = pitch, user=user)


@main.route('/delete_comment/<int:comment_id>', methods=['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment = Comments.query.filter_by(id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.home', comment_id=comment.id))



@main.route('/user/<name>', methods=['GET','POST'])
@login_required
def profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form=EditProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', name=user.username))
    return render_template('profile/profile.html', user=user, form=form)


@main.route('/user/<name>/edit/pic', methods=['POST'])
@login_required
def update_pic(name):
    user=User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar=path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))