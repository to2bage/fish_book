"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:18
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Blueprint
from flask import request
from flask import json, jsonify

from app.libs.helps import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from app.view_models.book import BookCollection
from app.forms.searchform import SearchForm

api = Blueprint("book", __name__)

# @api.route("/search/<string:q>/<int:page>")
# def search(q, page):
#     yushu_book = YushuBook()
#     yushu_book.search_by_keyword(q, page)
#     print(yushu_book.total)
#     print(yushu_book.books)
#     returned = {
#         "total": yushu_book.total,
#         "books": yushu_book.books
#     }
#     return jsonify(returned)
#     pass

# @api.route("/search/<string:q>/<int:page>")
# def search(q, page):
#     key_or_isbn = is_isbn_or_key(q)
#     yushu_book = YushuBook()
#     if key_or_isbn == "isbn":
#         yushu_book.search_by_isbn(q)
#     elif key_or_isbn == "keyword":
#         yushu_book.search_by_keyword(q, page)
#
#     book_collection = BookCollection()
#     book_collection.fill(yushu_book, q)
#
#     return json.dumps(book_collection, default=lambda o: o.__dict__)

@api.route("/search")
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data

        yushu = YushuBook()
        key_or_isbn = is_isbn_or_key(q)
        if key_or_isbn == "isbn":
            yushu.search_by_isbn(q)
        elif key_or_isbn == "keyword":
            yushu.search_by_keyword(q, page)

        book_collection = BookCollection()
        book_collection.fill(yushu, q)

        return json.dumps(book_collection, default=lambda o: o.__dict__)
    else:
        return form.errors
    pass
