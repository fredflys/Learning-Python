# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .commons import format_str


class CrawlSpiderPipeline(object):
    def __init__(self):
        self.file = open('tencent_positions', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        fmt = '{} {} {} {} {}\n'
        self.file.write(fmt.format(format_str(item['name'], 20),
                                   format_str(item['type'], 5),
                                   format_str(item['number'], 5),
                                   format_str(item['location'], 10),
                                   format_str(item['link'], 30),
                                   )
                        )
        return item

    def close_spider(self, spider):
        self.file.close()
