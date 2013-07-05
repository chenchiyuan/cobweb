# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from proxy import Cluster
from utils import requests
from utils import get_path
import json

class Client(object):
    def get_all_books(self, source="ZhangBook", limit=1, **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_all_books"
        }
        path = get_path(**params)
        data = kwargs
        data["limit"] = limit
        return requests(path, data=json.dumps(data))

    def get_book_detail(self, book_id, source="ZhangBook", cache=False, **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_book_detail"
        }
        path = get_path(**params)
        data = kwargs
        data["book_id"] = book_id
        data["cache"] = cache
        return requests(path, data=data)

    def get_chapters(self, book_id, start=1, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_chapters"
        }
        path = get_path(**params)
        data = kwargs
        data["book_id"] = book_id
        data["start"] = start
        return requests(path, data=data)

    def get_chapter_content(self, book_id, number_id, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_chapter_content"
        }
        path = get_path(**params)
        data = kwargs
        data["book_id"] = book_id
        data["number_id"] = number_id
        return requests(path, data=data)
