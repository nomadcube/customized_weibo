#! /usr/bin/env /Users/wumengling/PycharmProjects/customized_weibo/bin/python2.7
# coding=utf-8

import sys
import jieba

from hdfs import InsecureClient
from base import similarity

# 将"我的收藏"里的微博放入一个list中
hdfs_client = InsecureClient('http://127.0.0.1:50070')
my_favorites = list()
with hdfs_client.read('my_favorites.json') as reader:
    for line in reader:
        my_favorites.extend([w for w in jieba.cut(line, cut_all=True)])

for line in sys.stdin:
    line = line.strip("\n")
    one_post = [w for w in jieba.cut(line, cut_all=True)]
    print repr(similarity(one_post, my_favorites) / len(my_favorites)) + "," + line
