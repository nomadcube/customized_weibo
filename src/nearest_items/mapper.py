#! /usr/bin/env /Users/wumengling/PycharmProjects/customized_weibo/bin/python2.7
# coding=utf-8

import sys

from hdfs import InsecureClient


def similarity(a, b):
    one = set(a)
    other = set(b)
    return float(len(one.intersection(other))) / float(len(one.union(other)))


# 将"我的收藏"里的微博放入一个list中
hdfs_client = InsecureClient('http://127.0.0.1:50070')
my_favorites = list()
with hdfs_client.read('my_favorites.json') as reader:
    for line in reader:
        my_favorites.append([v for v in line.strip().decode("utf-8")])

for line in sys.stdin:
    cluster_similarity = 0.0
    line = line.strip("\n")
    one_post = [w for w in line.decode("utf-8")]
    for each_favorites in my_favorites:
        cluster_similarity += similarity(one_post, each_favorites)
    print repr(cluster_similarity / len(my_favorites)) + "," + line
