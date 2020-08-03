"""
Project name: fish_book
Description:
Create Time: 2020/8/3 13:07
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User

class RegisgerForm(Form):
    nickname = StringField(
        validators=[
            DataRequired(message="账户不可为空"),
            Length(min=2, max=10, message="账户字符限制[2, 10]")
        ]
    )
    password = PasswordField(
        validators=[
            DataRequired(message="密码不可为空"),
            Length(min=6, max=32, message="密码至少需要6个字符, 最多32个字符")
        ]
    )
    email = StringField(
        validators=[
            DataRequired(message="电子邮件不可为空"),
            Length(min=6, max=32),
            Email(message="电子邮件的格式不正确")
        ]
    )

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮件已经存在")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("账户已经存在")


class LoginForm(Form):
    email = StringField(
        validators=[
            DataRequired(message="电子邮件不可为空"),
            Length(min=6, max=32),
            Email(message="电子邮件的格式不正确")
        ]
    )

    password = PasswordField(
        validators=[
            DataRequired(message="密码不可为空"),
            Length(min=6, max=32, message="密码至少需要6个字符, 最多32个字符")
        ]
    )
