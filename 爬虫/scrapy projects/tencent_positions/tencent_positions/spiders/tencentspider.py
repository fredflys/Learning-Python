import scrapy
from .. import items


class TencentPositionsSpider(scrapy.Spider):
    name = 'tencentpositions'
    allowed_domains = ['hr.tencent.com', ]
    url = 'https://hr.tencent.com/position.php?start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even" or @class="odd"]'):
            item = items.TencentPositionsItem()

            item['name'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['link'] = TencentPositionsSpider.allowed_domain[0] + '/' + each.xpath('./td[1]/a/@href').extract()[0]
            item['type'] = each.xpath('./td[2]/text()').extract()[0]
            item['number'] = each.xpath('./td[3]/text()').extract()[0]
            item['location'] = each.xpath('./td[4]/text()').extract()[0]

            yield item

        if self.offset < 3880:
            self.offset += 10

        # 每次处理完一页的数据后，重新发送下一页的页面请求
        # 回调函数仍是self.parse
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)