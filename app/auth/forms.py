# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Имя пользователя'), validators=[DataRequired()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Запомнить меня'))
    submit = SubmitField(_l('Войти'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Имя'), validators=[DataRequired()])
    email = StringField(_l('Почта'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторите пароль'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Зарегистрироваться'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Упс! Это имя уже занято, пожалуйста, попробуйте другое.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Упс! Этот почтовый адрес уже кем-то используется, пожалуйста, попробуйте другую.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Ваш почтовый адрес'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Запросить восстановление пароля'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Введите новый пароль'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторите новый пароль'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Сменить пароль'))
