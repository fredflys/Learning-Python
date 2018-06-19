from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import os
from .. import items

# 从形如http://xxx.sina.com.cn/ruijian/的字符串中提取xxx
get_prefix_url = lambda url: url[url.find('/') + 2: url.find('.')]
# 去掉形如http://health.sina.com.cn/z/Aesculapiuswb/字符串中的文件名非法字符（用于从子分类的url中直接创建子文件夹）
get_subfolder_from_url = lambda url: url.replace('/', '').replace('http:', '').replace('?', '')


class SinanewsSpider(scrapy.Spider):
    name = 'sina_crawlspider'
    start_urls = ['http://news.sina.com.cn/guide/', ]

    # 用于提取出文章的url
    essay_info_extractor = LinkExtractor(restrict_xpaths='//a[re:match(@href, ".+\d+-\d+-\d+/.+.shtml")]/@href')
    rules = [
        Rule(LinkExtractor, follow=True, callback='parse_essay')
    ]
    category_list = []

    sub_category_dict = {}

    # 爬虫从这里开始，起点是新浪新闻的汇总页面
    def start_requests(self):
        return [scrapy.FormRequest(
                url='http://news.sina.com.cn/guide/',
                callback=self.prepare_folder)]

    def prepare_folder(self, response):
        """
        从汇总页面中提取出大类和小类，用于创建对应的层级文件夹
        并将分类信息加入到item中，方便之后存储到对应位置
        """
        all_items = []
        # 所有大类名称的列表
        # category_list = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/text()').extract()
        # 所有大类url的列表
        category_url_list = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/@href').extract()
        # 所有大类url前缀的列表
        # 并去除其中的房产和图片两个大类（房产下的url太不规则，图片也不在我们这次爬取的范围内）
        category_prefix_list = [get_prefix_url(href) for href in category_url_list if 'leju' not in href and 'photo' not in href]
        self.category_list = category_prefix_list

        # 提取出所有小类的url，规则中去掉了城市分类下的新闻
        sub_category_list = response.xpath('//div[@id="tab01"]//div[not(@data-sudaclick="citynav")]/h3[@class="tit02"]/following-sibling::*/li/a/@href').extract()
        sub_category_dict = {}
        for prefix in category_prefix_list:
            sub_category_dict[prefix] = []
        for index in range(len(sub_category_list)):
            sub_url = sub_category_list[index]
            sub_prefix = get_prefix_url(sub_url)
            # 以下的各种情况都是为了处理那些分类不遵循规则的小类url
            # 并不完整，但就先如此吧
            if 'video' in sub_url or 'data' in sub_url or 'photo' in sub_url or sub_prefix == 'www':
                pass
            elif index < 18:
                sub_category_dict['news'].append(sub_url)
            elif 'baby' in sub_url:
                sub_category_dict['baby'].append(sub_url)
            elif sub_prefix in ['golf', 'lottery', 'f1']:
                sub_category_dict['sports'].append(sub_url)
            elif sub_prefix in ['yue', 'dafen', 'yingxun', ]:
                sub_category_dict['ent'].append(sub_url)
            elif sub_prefix == 'roll':
                sub_category_dict['collection'].append(sub_url)
            else:
                if sub_prefix in category_prefix_list:
                    sub_category_dict[sub_prefix].append(sub_url)
                else:
                    pass
        self.sub_category_dict = sub_category_dict

        # 创建分类与子分类的文件夹
        base_dir = os.path.dirname(os.path.dirname(__file__)) + '\\data\\'
        for cate_name in self.category_list:
            if not os.path.exists(base_dir + cate_name):
                os.mkdir(base_dir + cate_name)
        for cate_name, sub_cate_list in self.sub_category_dict.items():
            for sub_cate_url in sub_cate_list:
                item = items.SinanewsAllItem()
                sub_cate_name = get_subfolder_from_url(sub_cate_url)
                sub_cate_path = base_dir + cate_name + '\\' + sub_cate_name
                if not os.path.exists(sub_cate_path):
                    os.mkdir(sub_cate_path)
                # 将当前迭代内的大类和子类的层级存入item的属性中，发送request
                # 并连带将item附带发出
                item['category'] = cate_name
                item['sub_category'] = sub_cate_name
                item['sub_category_url'] = sub_cate_url

                yield scrapy.Request(
                    url=sub_cate_url,
                    meta={'for_spider': item}, # 这里是item
                    callback=self.parse_sub_url
                )

    # 这是处理子类网页下的所有文章
    # 将由处理大类网页时带来item再度抛出，在之后处理文章时将会使用
    def parse_sub_url(self, response):
        item = response.meta['for_spider']
        # 从页面中提取中所有文章链接，其url中有xxxx-xx-xx的日期并以shtml结尾
        essay_list = response.xpath('//a[re:match(@href, ".+\d+-\d+-\d+/.+.shtml")]/@href').extract()
        for essay_url in essay_list:
            yield scrapy.Request(
                url=essay_url,
                meta={'for_spider': item},
                # 供CrawlSpider使用的提取规则也绑定了该回调函数
                # 在该迭代会对子分类下的所有文章发起请求
                # 因此都将携带有包裹着item的meta数据
                # item随着meta在request和response之间传递
                callback=self.parse_essay
            )

    # 真正提取文章信息的函数
    def parse_essay(self, response):
        item = response.meta['for_spider']
        possible_title_a = response.xpath('//h1[@class="main-title"]/text()').extract()
        possible_title_b = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()
        _ = possible_title_a or possible_title_b
        if _:
            title = _[0]
        else:
            title = ''
        import re
        content = ''
        _ = response.xpath('//div[@id="artibody"]').extract()
        if _:
            content = response.xpath('//div[@id="artibody"]').extract()[0]
            content = re.sub('<.+?>', '', content)
            content = re.sub('[\xa0\r\n\t\u3000]', '', content)
            content = re.sub('[(]function.+;', '', content).strip()

        item['url'] = response.url
        item['title'] = title
        item['content'] = content
        yield item
