# -*- coding: utf-8 -*-

# Scrapy settings for douban_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_spider'

SPIDER_MODULES = ['douban_spider.spiders']
NEWSPIDER_MODULE = 'douban_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DOUBAN_HEADER = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'movie.douban.com',
    'Referer':'https://www.douban.com/',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douban_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'douban_spider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DOUBAN_COOKIE = {
    'll':'108258',
    ' bid':'tJOA7FeSzTs',
    ' __utmt':'1',
    ' ps':'y',
    ' ue':'zhangqythu@gmail.com',
    ' dbcl2':'152319527:k/gLg4ZlWoM',
    ' ck':'FUX7',
    ' __utma':'30149280.963457478.1476021553.1476021553.1476088352.2',
    ' __utmb':'30149280.7.10.1476088352',
    ' __utmc':'30149280',
    ' __utmz':'30149280.1476088352.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    ' __utmv':'30149280.15231',
    ' __utma':'223695111.643052778.1476021571.1476021571.1476088586.2',
    ' __utmb':'223695111.0.10.1476088586',
    ' __utmc':'223695111',
    '__utmz':'223695111.1476088586.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    ' _pk_ref.100001.4cf6':'%5B%22%22%2C%22%22%2C1476088586%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    ' _pk_id.100001.4cf6':'484a762cc0d4b9a1.1476021571.2.1476088586.1476021597.',
    ' _pk_ses.100001.4cf6':'*',
    ' push_noty_num':'0',
    ' push_doumail_num':'0',
    ' _vwo_uuid_v2':'BA1DA8CF3D9B38A74F5A25F764994567|f3b2af6bc98aea0b8f9fbeca3f98fa1f',
}