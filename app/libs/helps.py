"""
Project name: fish_book
Description:
Create Time: 2020/7/31 09:57
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
def is_isbn_or_key(word):
    if len(word) == 13 and word.isdigit():
        return 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10:
        # isbn10
        return 'isbn'
    return 'keyword'
