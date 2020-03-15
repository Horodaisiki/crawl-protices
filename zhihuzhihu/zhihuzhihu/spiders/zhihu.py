# -*- coding: utf-8 -*-
import scrapy
from zhihuzhihu.items import ZhihuzhihuItem
import json
import lxml
import bs4


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url='https://www.zhihu.com/api/v4/questions/62972819/answers?include=data%5B*%5D.is_normal%2Ccontent&offset=0&limit=5&sort_by=updated'
        yield scrapy.Request(url, headers=self.headers)
    def parse(self, response):
        items=ZhihuzhihuItem()
        a=json.loads(response.body)
        b=a['data']
        for li in b:
            img=bs4.BeautifulSoup(li['content'],'lxml')
            ss=img.findAll('img')
            res=[]
            for lli in ss:
                if("data-original" in lli.attrs):
                    res.append(lli['data-original'])
        items['himg']=res
        yield items