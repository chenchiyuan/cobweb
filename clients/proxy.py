# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from conf import spiders
from conf import servers
import random

class Cluster(object):
    @classmethod
    def get_spider(cls):
        return random.choice(spiders)

    @classmethod
    def get_server(cls):
        return random.choice(servers)