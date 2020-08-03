"""
Project name: fish_book
Description:
Create Time: 2020/8/3 09:56
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

from contextlib import contextmanager

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as err:
            self.session.rollback()
            raise err


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = datetime.now().timestamp()

    def set_attr(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
