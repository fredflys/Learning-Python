import scrapy
from .. import items


class ImageSpider(scrapy.Spider):
    name = 'imagespider'
    allowed_domains = ['www.socwall.com']
    start_urls = ['https://www.socwall.com/wallpapers/page:1/', ]

    url = 'https://www.socwall.com/wallpapers/page:%s/'
    page_num = 1

    def parse(self, response):
        for each in response.xpath('//li[contains(@class, "wallpaper")]'):
            item = items.ImagespiderItem()

            item['title'] = each.xpath('./div/a/div/h2/text()').extract()[0]
            item['src'] = self.allowed_domains[0] + each.xpath('./div/a/img/@src').extract()[0]
            item['href'] = each.xpath('./div/a/@href').extract()[0]

            yield item

        # self.page_num += 1
        # yield scrapy.Request(self.url % self.page_num, callback=self.parse)
