import scrapy
from items import YousuuItems


class YousuuSpider(scrapy.Spider):
    name = 'yousuu'
    allowed_domains = ['www.yousuu.com', ]
    start_urls = ['http://www.yousuu.com/category/history?sort=rate&page=1', ]

    def parse(self, response):
        for each in response.xpath('//div[@class="col-md-6 col-sm-12"]'):
            item = YousuuItems()

            title = each.xpath('.//div[@class="title"]/a/text()').extract()[0].strip()

            info_list = each.xpath('.//div[@class="abstract"]/text()').extract()
            writer = info_list[0][4:]
            words = info_list[1][4:]
            rate = each.xpath('.//div[@class="abstract"]/span/text()').extract()[0]

            item['title'] = title
            item['writer'] = writer
            item['words'] = words
            item['rate'] = rate

            yield item





