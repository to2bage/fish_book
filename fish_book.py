"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:15
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()