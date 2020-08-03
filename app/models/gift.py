"""
Project name: fish_book
Description:
Create Time: 2020/8/3 09:56
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)