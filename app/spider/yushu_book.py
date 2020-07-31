"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:43
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import current_app

from app.libs.http import HTTP


class YushuBook():
    def __init__(self):
        self.books = []
        self.total = 0
        self.per_page = current_app.config["PER_PAGE"]
        self.isbn_url = current_app.config["ISBN_URL"]
        self.keyword_url = current_app.config["KEYWORD_URL"]

    def search_by_isbn(self, keyword):
        url = self.isbn_url.format(keyword)
        result = HTTP.get(url)
        self.__fill_single_data(result)

    def search_by_keyword(self,keyword, page=1):
        page = int(page)
        url = self.keyword_url.format(keyword, self.per_page, (page-1)*self.per_page)
        result = HTTP.get(url)
        self.__fill_collection_data(result)

    def __fill_single_data(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection_data(self, data):
        if data:
            self.total = data["total"]
            self.books = data["books"]



class _YushuBook():
    def __init__(self, app):
        self.books = []
        self.total = 0
        self.current_app = app
        self.per_page = current_app.config["PER_PAGE"]
        self.isbn_url = current_app.config["ISBN_URL"]
        self.keyword_url = current_app.config["KEYWORD_URL"]

    def search_by_isbn(self, keyword):
        url = self.isbn_url.format(keyword)
        result = HTTP.get(url)
        self.__fill_single_data(result)

    def search_by_keyword(self,keyword, page):
        page = int(page)
        url = self.keyword_url.format(keyword, self.per_page, (page-1)*self.per_page)
        result = HTTP.get(url)
        self.__fill_collection_data(result)

    def __fill_single_data(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection_data(self, data):
        if data:
            self.total = data["total"]
            self.books = data["books"]


