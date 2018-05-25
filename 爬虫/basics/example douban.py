"""
爬虫最应该关注的不是页面显示什么，而是数据的来源
Ajax方式加载的页面，数据来源一定是json
"""

from urllib import request
from urllib import parse
from fake_useragent import UserAgent
import json

category_dict = {'1': '纪录片', '2': '传记', '3': '犯罪', '4': '历史', '5': '动作', '6': '情色', '7': '歌舞', '8': '儿童', '10': '悬疑', '11': '剧情', '12': '灾难', '13': '爱情', '14': '音乐', '15': '冒险', '16': '奇幻', '17': '科幻', '18': '运动', '19': '惊悚', '20': '恐怖', '22': '战争', '23': '短片', '24': '喜剧', '25': '动画', '26': '同性', '27': '西部', '28': '家庭', '29': '武侠', '30': '古装', '31': '黑色电影'}


def fake_ua():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }
    return headers


def get_json(category_num, start, end):
    url = "https://movie.douban.com/j/chart/top_list?type=" + category_num + "&interval_id=100%3A90&action="
    # url = "https://movie.douban.com/typerank?" + encoded_type + "&type=" + category_num + "&interval_id=100:90&action="
    paras = "&start=%s&limit=%s" % (start-1, end-start+1)
    request_config = request.Request(url+paras, headers=fake_ua())
    json_response = request.urlopen(request_config).read()
    return json_response


def display_json(json_data):
    info_list = json.loads(json_data)
    for item_dict in info_list:
        rank = item_dict['rank']
        title = item_dict['title']
        regions = item_dict['regions'][0]
        rating = item_dict['rating'][0]
        release_date = item_dict['release_date']
        print(rank, title, regions, rating, release_date)


if __name__ == "__main__":
    for k in category_dict:
        print(k, category_dict[k])
    cate_num = input("请输入要查看的类别编号：")
    start = int(input("请输入起始序号："))
    end = int(input('请输入结束序号：'))
    json_response = get_json(cate_num, start, end)
    display_json(json_response)
