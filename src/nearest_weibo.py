# coding=utf-8
from io import open

import numpy as np
from src.map_reduce.base import jaccard_similarity


def cluster_similarity(doc, doc_cluster):
    """
    计算单个文档与特定文档类的相似度
    用平均Jaccard相似度作为相似度度量

    :param doc: list of str, 单个文档
    :param doc_cluster: list of list, 一个文档类
    :return: float, 单个文档和文档类的相似度
    """
    similarity = 0.0
    for one_doc in doc_cluster:
        similarity += jaccard_similarity(doc, one_doc)
    return similarity / len(doc_cluster)


def nearest_weibo_index(latest_timeline, favorites):
    """
    从最新的微博信息流中选出和"我的收藏"最接近的微博

    :param latest_timeline: list, 最新的微博信息流
    :param favorites: list, "我的收藏"中的微博
    :param k: int, 确定相似度最高的前k条信息流微博中的k值
    :return: list, 和"我的收藏"最接近的微博在微博信息流中的k个行号
    """
    scores = np.zeros(len(latest_timeline))
    for ind, each_timeline in enumerate(latest_timeline):
        scores[ind] = cluster_similarity(each_timeline, favorites)
    return np.argmax(scores)


def find_original_weibo(latest_file, index):
    """
    从最新微博信息流中获取第index条微博

    :param latest_file: str, 微博信息流的文件名
    :param index: int, 和"我的收藏"最相近的微博行号
    :return: str, 和"我的收藏"最相近的的微博内容
    """
    with open(latest_file, 'r', encoding="utf-8") as f:
        return f.readlines()[index]
