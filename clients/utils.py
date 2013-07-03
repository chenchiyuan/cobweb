# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from conf import routers, http_headers

import requests as py_requests

def get_path(host, port, source, path):
    path_lambda = lambda host, port, source, path: \
        "{host}:{port}/{source}/{path}".format(host=host, port=port,
            source=source.lower(), path=path)
    real_path = routers.get(path, path)
    return path_lambda(host, port, source, real_path)

def requests(url, method="get", **kwargs):
    handler = getattr(py_requests, method, py_requests.get)
    content = handler(url=url, headers=http_headers ,**kwargs).content
    return content