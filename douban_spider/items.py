# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() # 电影名
    director = scrapy.Field() # 电影导演
    starring = scrapy.Field() # 电影主演
    _type = scrapy.Field() # 电影类型
    post = scrapy.Field() # 电影海报
    _id = scrapy.Field() # 防止重复申请
    score = scrapy.Field() # 豆瓣评分