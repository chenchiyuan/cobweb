# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

spiders = [
    {
        "host": "http://127.0.0.1",
        "port": 9998,
    }
]

servers = [
    {
        "host": "http://127.0.0.1",
        "port": 9999
    }
]

routers = {
    "get_all_books": "books/",
    "get_book_detail": "book/detail/",
    "get_chapters": "chapters/",
    "get_chapter_content": "chapter/detail/",
}

http_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7a) Gecko/20050614 Firefox/0.9.0+",
}