# coding=utf-8
import jieba
from base import similarity


sentence = u'腾讯里养了只喵'
with open('/Users/wumengling/PycharmProjects/customized_weibo/src/nearest_items/test_data.txt', 'r') as f:
    for line in f.readlines():
        line_vec = jieba.cut(line, cut_all=True)
        sentence_vec = jieba.cut(sentence, cut_all=True)
        print similarity(line_vec, sentence_vec)
