import scraper_helper as sh

BOT_NAME = 'webscrapping'

SPIDER_MODULES = ['webscrapping.spiders']
NEWSPIDER_MODULE = 'webscrapping.spiders'

DEFAULT_REQUEST_HEADERS = sh.get_dict(
    '''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    cookie: session-id=257-3909243-2628847; i18n-prefs=INR; ubid-acbin=262-7437873-4745361; session-token=HdQUK3lr1AtABWaHAUUdW4CZNzFnAxuemJ/RF4Phm3Ym4M8jFWAzsHTn8XeOVhVi8jjJLY8lSkYNmgoX1i9fJVAWqciL/8c2thnzXEMLgP7AKgsxOmjpdq8AXMullTCgMjf2xX9wT/4P4v5jYE+roaH9a3Kk9axauYmIY+aTtQSzFfuZxmZ0TGvDFW5GjGfMISpcN84LdYw1IcY2X0WH4XVIKzIiLnB5HLwhsvBs+67Cn/v0xzH272ja7Re6fRc+; session-id-time=2082758401l; csm-hit=tb:285VB308NS996DX5Z667+s-285VB308NS996DX5Z667|1648989706767&t:1648989706767&adb:adblk_no
    device-memory: 8
    dnt: 1
    downlink: 10
    dpr: 1
    ect: 4g
    rtt: 150
    sec-ch-device-memory: 8
    sec-ch-dpr: 1
    sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-ch-viewport-width: 1440
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: none
    sec-fetch-user: ?1
    service-worker-navigation-preload: true
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36
    viewport-width: 1440
    '''
)
AUTOTHROTTLE_ENABLED = True

ROBOTSTXT_OBEY = False

# PROXY_POOL_ENABLED = True

# DOWNLOADER_MIDDLEWARES = {
#     # ...
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
#     # ...
# }

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'webscrapping.middlewares.WebscrappingSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'webscrapping.middlewares.WebscrappingDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'webscrapping.pipelines.WebscrappingPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
