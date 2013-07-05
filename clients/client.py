# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from proxy import Cluster
from utils import requests
from utils import get_path

class Client(object):
    def get_all_books(self, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_all_books"
        }
        path = get_path(**params)
        return requests(path)

    def get_book_detail(self, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_book_detail"
        }
        path = get_path(**params)
        return requests(path)

    def get_chapters(self, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_chapters"
        }
        path = get_path(**params)
        return requests(path)

    def get_chapter_content(self, source="ZhangBook", **kwargs):
        spider = Cluster.get_spider()
        params = {
            "host": spider['host'],
            "port": spider['port'],
            "source": source,
            "path": "get_chapter_content"
        }
        path = get_path(**params)
        return requests(path)
