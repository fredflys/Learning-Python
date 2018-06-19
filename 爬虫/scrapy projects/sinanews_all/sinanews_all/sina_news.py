

class o:

    start_urls = ['http://news.sina.com.cn/guide/', ]

    subtype_extractor = LinkExtractor(restrict_xpaths='//div[@id="tab01"]//div[not(@data-sudaclick="citynav")]/h3[@class="tit02"]/following-sibling::*')
    rules = [
        Rule(subtype_extractor, follow=True, callback='parse_subtype')
    ]
    category_dict = {}

    def start_requests(self):
        return [scrapy.FormRequest(
                url='http://news.sina.com.cn/guide/',
                callback=self.prepare_folder
            )
        ]



    def parse_subtype(self, response):
        print(response.url)