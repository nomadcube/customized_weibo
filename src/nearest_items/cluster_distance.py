# coding=utf-8
from map_reduce.base import jaccard_similarity


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
