"""
Project name: fish_book
Description:
Create Time: 2020/7/31 13:35
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class SearchForm(Form):
    q = StringField(
        validators=[
            DataRequired(message="关键字是必填项目"),
            Length(min=1, max=30, message="关键字有长度的要求: [1, 30]")
        ]
    )
    page = IntegerField(
        validators=[
            NumberRange(min=1, max=99, message="页码的范围: [1, 99]")
        ], default=1
    )
