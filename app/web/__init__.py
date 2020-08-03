"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:18
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Blueprint

web = Blueprint("web", __name__, template_folder="templates")

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish