import requests
from xml.etree import ElementTree as ET
# 使用webxml的列车信息表，读取某一车次的信息

# 使用第三方模块requests发送HTTP请求
r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?Traincode=K234&UserID= ')
result = r.text

# 将字符串解析为XML格式内容
root = ET.XML(result)

print(result)
# 通过iter方法在子孙节点迭代的寻找某一个节点
for node in root.iter('TrainDetailInfo'):
    # print(node.tag,node.attrib) 获取节点标签和属性
    # find是在子节点重寻找
   print(node.find('TrainStation').text, node.find('StartTime').text) #获取标签内容

# root.iter的解释
# for node in root:
#     print(node)
#     for node_node in node:
#         for node_node_node in node_node:
#             print(node_node_node)
