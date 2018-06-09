# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class WallpaperPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGE_STORE")

    def get_media_requests(self, item, info):
        src = item['src']
        yield scrapy.Request(src)

    def item_completed(self, results, item, info):
        img_path = [x['path'] for ok, x in results if ok]
        item['img_path'] = img_path[0]
        return item
