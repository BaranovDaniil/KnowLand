# -*- coding: utf-8 -*-
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Имя пользовтеля'), validators=[DataRequired()])
    about_me = TextAreaField(_l('Расскажите о себе'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Создать'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Упс! Это имя уже занято, пожалуйста используйте другое.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Здесь вас услышат'), validators=[DataRequired()])
    submit = SubmitField(_l('Публиковать'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
