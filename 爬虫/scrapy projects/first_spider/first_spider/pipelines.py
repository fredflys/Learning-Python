# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from commons import format_str


class YousuuPipeline(object):
    def __init__(self):
        self.file = open("book_info", "a", encoding='utf-8')

    def process_item(self, item, spider):
        fmt = '{} {} {} {}\n'
        self.file.write(fmt.format(format_str(item['title'], 35),
                                   format_str(item['rate'], 5),
                                   format_str(item['words'], 10),
                                   format_str(item['writer'], 10)
                                   )
                        )

    def close_spider(self, spider):
        self.file.close()
