from .. import items
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

from fake_useragent import UserAgent as UA
import os
from urllib.request import urlretrieve
from PIL import Image


class TopMoviesSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['www.douban.com', 'movie.douban.com', 'accounts.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0', ]
    # 生成随机的User Agent
    headers = {'User-Agent': UA().random}

    # 定义页面提取规则
    page_extractor = LinkExtractor(allow=('start=\d*',))
    rules = [
        Rule(page_extractor, follow=True, callback='parse_movie_info')
    ]

    # 开始处理请求，首先发起登陆请求
    def start_requests(self):
        return [
            scrapy.FormRequest(
                url="https://accounts.douban.com/login",
                headers=self.headers,
                meta={"cookiejar": 1},
                callback=self.login_douban
                )
            ]

    # 从响应的登陆页面获取captcha-id，这是之后发送post请求时的必要参数之一
    def login_douban(self, response):
        # 获取captcha-id与验证码的图片地址
        captcha_id = response.xpath('//input[@name="captcha-id"]/@value').extract()

        # 准备基本的formdata
        formdata = {
            'source': 'None',
            'form_email': input('请输入账户名：'),
            'form_password': input('请输入密码：'),
            'login': '登录'
        }
        if captcha_id:
            captcha_id = captcha_id[0]
            captcha_url = response.xpath('//img[@id="captcha_image"]/@src').extract()[0]
            # 有验证码图片地址则去下载验证码图片到本地
            captcha_path = os.path.dirname(os.path.dirname(__file__)) + '/captcha-images/captcha.jpg'
            urlretrieve(captcha_url, captcha_path)
            # 确保验证码图片下载成功
            try:
                image = Image.open(captcha_path)
                image.show()
                captcha_solution = input('请输入验证码: ')
                formdata['captcha-id'] = captcha_id
                formdata['captcha-solution'] = captcha_solution
            except FileNotFoundError:
                pass
        # 登陆完成后，携带cookie访问待爬取页面
        return scrapy.FormRequest.from_response(
            response,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata=formdata,
            callback=self.start_parse
        )

    # 开始爬取电影页面，一旦页面中有符合规则的数据就调用其回调函数进行处理，产生item
    def start_parse(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_movie_info(self, response):
        movies_in_page = response.xpath('//div[@class="info"]')
        for each in movies_in_page:
            item = items.DoubanMovieItem()
            item['title'] = each.xpath('.//span[@class="title"][1]/text()').extract()[0].replace('\n', '').replace('\xa0', '').strip()
            item['info'] = each.xpath('./div[@class="bd"]/p/text()').extract()[0]
            item['score'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = each.xpath('.//p[@class="quote"]/span/text()').extract()
            if quote:
                item['quote'] = quote[0].replace('\xa0', '').strip()
            else:
                item['quote'] = ''
            yield item





