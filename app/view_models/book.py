"""
Project name: fish_book
Description:
Create Time: 2020/7/31 09:43
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""

class BookViewModel:
    def __init__(self, data):
        self.title = data["title"]
        self.author = ", ".join(data["author"])
        self.binding = data["binding"] or ""
        self.publisher = data['publisher']
        self.image = data['image']
        self.price = data["price"] or ""
        self.isbn = data["isbn"]
        self.pubdate = data["pubdate"]
        self.summary = data["summary"] or ""
        self.pages = data["pages"] or ""

    @property
    def intro(self):
        li = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return " / ".join(li)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword