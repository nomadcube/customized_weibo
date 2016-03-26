# coding=utf-8
import re

from json import load
from weibo import Client
from io import open


def craw_save_clean_corpus(n=2):
    """
    将抓取回来的微博存入本地作为语料库

    :param n: int, 决定n元语法中n的值
    :return: NULL
    """
    raw_favorites = craw_raw_data('favorites')
    raw_latest_posts = craw_raw_data('statuses/friends_timeline')

    with open("/Users/wumengling/PycharmProjects/customized_weibo/data/favorites.txt", "w", encoding="utf-8") as f:
        for one_post in raw_favorites[u'favorites']:
            if one_post['status'].get('retweeted_status') is not None:
                text_id = one_post['status']['retweeted_status']['id']
                text = n_gram(clean_format(one_post['status']['retweeted_status']['text']), n)
            else:
                text_id = one_post['status']['id']
                text = n_gram(clean_format(one_post['status']['text']), n)
            f.write(str(text_id) + "||" + " ".join(text) + "\n")

    with open("/Users/wumengling/PycharmProjects/customized_weibo/data/latests.txt", "w", encoding="utf-8") as f:
        for one_post in raw_latest_posts[u'statuses']:
            if one_post.get('retweeted_status') is not None:
                text_id = one_post['retweeted_status']['id']
                text = n_gram(clean_format(one_post['retweeted_status']['text']), 2)
            else:
                text_id = one_post['id']
                text = n_gram(clean_format(one_post['text']), 2)
            f.write(str(text_id) + "||" + " ".join(text) + "\n")


def craw_raw_data(api_name):
    """
    通过微博的API抓取数据

    :param api_name: str
    :return: unicode
    """
    with open('/Users/wumengling/PycharmProjects/customized_weibo/config/weibo_config.json', 'r') as weibo_config_file:
        weibo_config = load(weibo_config_file)
        oauth_client = Client(weibo_config['API_KEY'], weibo_config['API_SECRET'], weibo_config['REDIRECT_URI'],
                              weibo_config['TOKEN'])
    return oauth_client.get(api_name, uid='1860068802')


def n_gram(sentence, n):
    """
    对文档进行n元语法处理

    :param sentence: str, 待处理的句子/文章
    :param n: int, 决定n的值
    :return: list, 由各项表示的文档
    """
    return [sentence[unit_index:unit_index + n] for unit_index in xrange(len(sentence) - n + 1)]


def clean_format(sentence):
    """
    将sentence中所有的标点符号/空格/换行符去掉

    :param sentence: str, 待处理的句子/文章
    :return: str, 处理完成后的句子/文章
    """
    sentence = re.sub("/", "", sentence)
    sentence = re.sub(u"，", "", sentence)
    sentence = re.sub(u" ", "", sentence)
    sentence = re.sub(u"：", "", sentence)
    sentence = re.sub(u"\"", "", sentence)
    sentence = re.sub("\n", "", sentence)
    return sentence


if __name__ == '__main__':
    print n_gram(u'对文档进行n 元语,法处理', 2)
    print clean_format(u'# 京 东 手 机 圈 #   H T C   1 0 跑 分 真 逆 天 了 ， 目 前 还 没 其 他 对 手 ？ \n外 媒 曝 光 了 一 张 H T C   1 0 安 兔 兔 跑 分 的 谍 照 ， 高 达 1 5 万 余 分 的 成 绩 再 次 刷 新 了 跑 分 纪 录 ， 强 的 也 是 没 谁 了 。 [ 给 力 ] 这 是 否 能 激 起 小 伙 伴 们 的 欲 望 呢 ？')
