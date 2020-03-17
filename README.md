# crawl-proctices
一些微不足道的爬虫实践


- pc-pixivic.py是对图片网站pixivic.com的爬取，采用的是异步爬取，直接请求的json接口
- pc-SignupForDouban.py是模拟登陆豆瓣的尝试，没有使用scrapy，用的请求登陆接口验证返回信息，在使用cookies登陆
- scrapy框架
- - zhihuzhihu是对知乎上答案的爬取，采用的异步爬取，问题编号需要自己去找，不需要登陆
- - Douban是用scrapy使用中间件登陆并获取cookie登陆的尝试
