"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:36
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        resp = requests.get(url)
        if resp.status_code != 200:
            return {} if return_json else ""
        return resp.json() if return_json else resp.text
