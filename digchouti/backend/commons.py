#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import time
import random
import collections


def random_code():
    code = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        code += str(temp)
    return code


def generate_md5(value):
    r = str(time.time())
    obj = hashlib.md5(r.encode('utf-8'))
    obj.update(value.encode('utf-8'))
    return obj.hexdigest()


# d_dic: 要查找的字典
# comment_obj: 要搜索的元组
def tree_search(d_dic, comment_obj):
    # 在comment_dic中一个一个的寻找其回复的评论
    # 检查当前评论的 reply_id 和 comment_dic中已有评论的nid是否相同，
    #   如果相同，表示就是回复的此信息
    #   如果不同，则需要去 comment_dic 的所有子元素中寻找，一直找，如果一系列中未找，则继续向下找
    for k, v_dic in d_dic.items():
        # 找回复的评论，将自己添加到其对应的字典中，例如： {评论一： {回复一：{},回复二：{}}}
        ''' d_dic = 
            {
            (评论ID，评论内容，评论对象):{},
            (评论ID，评论内容，评论对象):{},
            }
        '''
        # 如果评论ID和评论对象一致，就在该评论下创建有序字典
        if k[0] == comment_obj[2]:
            d_dic[k][comment_obj] = collections.OrderedDict()
            return
        else:
            # 在当前第一个根元素中递归的去寻找父亲
            # 会搜索当前元素对应的字典中的所有元素及其子孙元素（递归遍历）
            # for循环会保证当前节点下的所有兄弟元素被遍历到
            tree_search(d_dic[k], comment_obj)

        '''
        comment_list = [
            (1, '111',None),
            (2, '222',None),
            (3, '33',None),
            (4, '444',2),
            (5, '555',1),
            (6, '666',4),
            (7, '777',2),
            (8, '888',4),
            (9, '999',5),
        ]  #(评论ID，评论内容，评论对象) None表示对新闻的评论

        形成的评论应该如下：
        News......
        1
          5
            9
        2
          4
            8
          7
            6
        3
        '''


def build_tree(comment_list):
    # 有序字典
    # 评论对象必须预先存在才可以评论
    comment_dic = collections.OrderedDict()

    for comment_obj in comment_list:
        # (评论ID，评论内容，评论对象)  None表示是根评论
        if comment_obj[2] is None:
            # 如果是根评论，添加到comment_dic[评论对象] ＝ {}
            comment_dic[comment_obj] = collections.OrderedDict()
        else:
            # 如果是回复的评论，则需要在 comment_dic 中找到其回复的评论
            tree_search(comment_dic, comment_obj)
    return comment_dic

