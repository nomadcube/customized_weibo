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


if __name__ == '__main__':
    client = InsecureClient('http://127.0.0.1:50070')
    raw_favorites = craw_raw_data('favorites')
    raw_latest_posts = craw_raw_data('statuses/friends_timeline')

    client.delete('latest_posts.json')
    client.delete('my_favorites.json')

    with client.write('my_favorites.json', encoding='utf-8') as writer:
        for one_post in raw_favorites[u'favorites']:
            writer.write(one_post['status']['text'] + "\n")

    with client.write('latest_posts.json', encoding='utf-8') as writer:
        for one_post in raw_latest_posts[u'statuses']:
            writer.write(one_post['text'] + "\n")
