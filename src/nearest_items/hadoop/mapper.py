#! /usr/bin/env /Users/wumengling/PycharmProjects/customized_weibo/bin/python2.7
# coding=utf-8

import sys

from hdfs import InsecureClient
from src.nearest_items.hadoop.base import similarity

# 将"我的收藏"里的微博放入一个list中
hdfs_client = InsecureClient('http://127.0.0.1:50070')
my_favorites = list()
with hdfs_client.read('my_favorites.json') as reader:
    for line in reader:
        my_favorites.extend(line.strip().split(" "))

for line in sys.stdin:
    line = line.strip("\n")
    one_post = line.strip().split(" ")
    print repr(similarity(one_post, my_favorites) / len(my_favorites)) + "," + line
