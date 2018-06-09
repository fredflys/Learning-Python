from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .. import items

count = 0

class AffairsSpider(CrawlSpider):
    name = 'citizen_affairs'
    allowed_domains = ['wz.sun0769.com', ]
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0', ]

    page_extractor = LinkExtractor(allow=(r'page=\d+', ), )

    question_extractor = LinkExtractor(allow=(r'/question/\d+/\d+\.shtml', ))

    rules = [
        Rule(page_extractor, follow=True),
        Rule(question_extractor, callback='parse_posts', follow=False)
    ]

    def parse_posts(self, response):
        item = items.CitizenAffairsItem()

        info_list = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0].split('\xa0\xa0')
        item['title'] = info_list[0].split('提问')[1][1::]
        item['identifier'] = info_list[1].split('编号')[1][1::]

        content = ''
        content_list = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
        if len(content_list) > 1:
            for element in content_list:
                content += element
        else:
            if content_list[0] == '\xa0\xa0\xa0\xa0':
                content = response.xpath('//div[@class="contentext"]/text()').extract()[0]
        content = content.replace('\xa0', '').replace('\n', '').strip()
        item['content'] = content

        print(item)
        global count
        count += 1
        print(count)
        yield item