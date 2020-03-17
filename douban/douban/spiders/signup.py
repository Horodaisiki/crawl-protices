# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
import json
import bs4
import lxml

class SignupSpider(scrapy.Spider):
    name = 'signup'
    item = DoubanItem()
    allowed_domains = ['douban.com']
    urls = ['https://movie.douban.com/chart']

    def start_requests(self):
        url = 'https://accounts.douban.com/j/mobile/login/basic'
        headers = {
            "Accept": "application/json",
            "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
            "Host": "accounts.douban.com",
        }
        data = {
            "name": "*********",
            "password": "********",
            "remeber": "False",
            "ck": "",
            "ticket": ""
        }
        yield scrapy.FormRequest(url, formdata=data,meta={"cookiejar":1}, callback=self.parse)
        return super().start_requests()
    def parse(self, response):
        yield scrapy.Request(self.urls[0],callback=self.parse_page)

    def parse_page(self, response):
        print(response.status)
        b=bs4.BeautifulSoup(response.text,"lxml")
        print('='*30)
        print(b.text)
        print('='*30)
        
