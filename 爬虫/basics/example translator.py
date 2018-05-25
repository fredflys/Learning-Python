"""
Get 请求的url会附带查询参数，参数在QueryString中存储
Post 查询参数在form表单中保存

http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
i=python
&from=AUTO
&to=AUTO
&smartresult=dict
&client=fanyideskweb
&salt=1527075778580
&sign=aeea5883bacb755c7e4a8f9b867c2bab
&doctype=json
&version=2.1
&keyfrom=fanyi.web
&action=FY_BY_CLICKBUTTION
&typoResult=false
"""
from urllib import request
from urllib import parse
from fake_useragent import UserAgent
import json


def fake_ua():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    return headers


def post_to_translator(source):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    form_data = {
        "type": "AUTO",
        "i": source,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "true",
    }
    data = parse.urlencode(form_data)
    request_config = request.Request(url, headers=fake_ua(), data=bytes(data, encoding='utf-8'))
    response = request.urlopen(request_config)
    return response.read()


def parse_response(response_json):
    response_dict = json.loads(response_json)
    return response_dict['translateResult'][0][0]['tgt']


if __name__ == "__main__":
    source = input('Please enter words to be translated: ')
    response_json = post_to_translator(source)
    result = parse_response(response_json)
    print('Result: ', result)
    