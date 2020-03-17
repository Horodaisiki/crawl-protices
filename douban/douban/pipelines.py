# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):
    def process_item(self, item, spider):
        
        with open('cookies.json',"r") as re:
            a=json.loads(re.read())
        a['cookies'].append(item['cookies'])
        return item
