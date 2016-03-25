# coding=utf-8
from json import load
from weibo import Client
from hdfs import InsecureClient


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


def save_corpus(n=2):
    """
    将抓取回来的微博存入hdfs作为语料库

    :param n: int, 决定n元语法中n的值
    :return: NULL
    """
    client = InsecureClient('http://127.0.0.1:50070')
    raw_favorites = craw_raw_data('favorites')
    raw_latest_posts = craw_raw_data('statuses/friends_timeline')

    client.delete('latest_posts.json')
    client.delete('my_favorites.json')

    with client.write('my_favorites.json', encoding='utf-8') as writer:
        for one_post in raw_favorites[u'favorites']:
            if one_post['status'].get('retweeted_status') is not None:
                writer.write(" ".join(n_gram(one_post['status']['retweeted_status']['text'], n)) + "\n")
            else:
                writer.write(" ".join(n_gram(one_post['status']['text'], n)) + "\n")

    with client.write('latest_posts.json', encoding='utf-8') as writer:
        for one_post in raw_latest_posts[u'statuses']:
            if one_post.get('retweeted_status') is not None:
                writer.write(" ".join(n_gram(one_post['retweeted_status']['text'], n)) + "\n")
            else:
                writer.write(" ".join(n_gram(one_post['text'], n)) + "\n")


if __name__ == '__main__':
    print n_gram(u'对文档进行n元语法处理', 2)
    save_corpus(2)
