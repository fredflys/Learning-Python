# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *


class DoubanMongodbPipeline(object):
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        datatable = MONGODB_TABLE

        client = pymongo.MongoClient(host=host, port=port)
        database = client[dbname]

        # 指定存放数据库的数据表
        self.db_table = database[datatable]

    def process_item(self, item, spider):
        self.db_table.insert(dict(item))
