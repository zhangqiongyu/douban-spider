#!/usr/bin/env/ python
# -×-coding: utf-8 -*-
#Creating a spider

import scrapy
import re
from bs4 import BeautifulSoup
from douban_spider.setting import *
from douban_spider.items import DoubanSpiderItem
from scrapy.http import Request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/subject/26374205/?from=showing']
    allow_domain = ['https://movie.douban.com/']

    def __init__(self, **kwargs):
        super(DoubanSpider, self).__init__(self, **kwargs)
        self.base_url = 'https://movie.douban.com/'
        # self.movies_url = 'https://movie.douban.com/node/hehe'

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(self, url)
    
    def make_requests_from_url(self, url):
        return Request(url, method='GET', headers=DOUBAN_HEADER, cookies=DOUBAN_COOKIE)
    
    def parse(self, response):
        item = DoubanSpiderItem()
        name = response.css()
