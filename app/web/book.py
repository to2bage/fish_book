"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:18
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Blueprint, render_template
from flask import request, flash
from flask import json, jsonify

from app.web import web
from app.libs.helps import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from app.view_models.book import BookCollection, BookViewModel
from app.forms.searchform import SearchForm


# @web.route("/book/search/<string:q>/<int:page>")
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

# @web.route("/book/search/<string:q>/<int:page>")
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

@web.route("/book/search")
def search():
    """
    /book/search?q=金庸&page=1
    :return:
    """
    form = SearchForm(request.args)
    book_collection = BookCollection()
    if form.validate():
        q = form.q.data
        page = form.page.data

        yushu = YushuBook()
        key_or_isbn = is_isbn_or_key(q)
        if key_or_isbn == "isbn":
            yushu.search_by_isbn(q)
        elif key_or_isbn == "keyword":
            yushu.search_by_keyword(q, page)

        book_collection.fill(yushu, q)
    else:
        flash("搜索的关键字不符合要求, 请重新输入关键字")
        # print(form.errors)
    return render_template("search_result.html", books=book_collection)

@web.route("/book/<string:isbn>/detail")
def book_detail(isbn):
    yushu_book = YushuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template("book_detail.html", book=book, wishes=[], gifts=[])
    pass

# @web.route("/test")
# def test():
#     r = {
#         "name": "to2bage",
#         "age": 45
#     }
#     return render_template("test.html", data = r)
