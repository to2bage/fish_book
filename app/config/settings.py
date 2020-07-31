"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:16
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
# 请求API
KEYWORD_URL = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"
ISBN_URL = "http://t.yushu.im/v2/book/isbn/{}"

URL1 = "http://t.yushu.im/v2/book/search?q=金庸&count=15"
URL2 = "http://t.yushu.im/v2/book/isbn/9787070511209"

# 每一页显示数据量
PER_PAGE = 15