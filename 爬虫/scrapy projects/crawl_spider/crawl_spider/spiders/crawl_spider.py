import scrapy
from .. import items

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentPositionsSpider(CrawlSpider):
    name = 'tencentpositions'
    allowed_domains = ['hr.tencent.com', ]
    start_urls = ['https://hr.tencent.com/position.php?start=', ]

    page_extractor = LinkExtractor(allow=('start=\d+'))

    rules = [
        Rule(
            page_extractor, callback='parse_pages', follow=True
        )
    ]

    # 方法名不可为parse，已被Spider占用
    def parse_pages(self, response):
        for each in response.xpath('//tr[@class="even" or @class="odd"]'):
            item = items.TencentPositionsItem()

            item['name'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['link'] = TencentPositionsSpider.allowed_domains[0] + '/' + each.xpath('./td[1]/a/@href').extract()[0]
            item['type'] = each.xpath('./td[2]/text()').extract()[0]
            item['number'] = each.xpath('./td[3]/text()').extract()[0]
            item['location'] = each.xpath('./td[4]/text()').extract()[0]

            yield item
