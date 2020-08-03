"""
Project name: fish_book
Description:
Create Time: 2020/8/3 09:56
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.base import Base



class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column("password", String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_txt):
        self._password = generate_password_hash(plain_txt)

    def check_pwd(self, plain_pwd):
        return check_password_hash(self._password, plain_pwd)



#  为了能使用login_requered
# @login_manager.user_loader
# def get_user(uid):
#     return User.query.get(int(uid))
