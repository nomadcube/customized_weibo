# coding=utf-8
import pymongo

from weibo import Client
from json import load


def create_favorite(weibo_index, mongo_obj_index_list):
    """
    通过微博写入接口，将微博id为id的信息流加入"我的收藏"

    :param weibo_index: str, 微博id对应的字符串
    :param mongo_obj_index_list: list, 由序列化后在mongodb中的object_id组成
    :return: NULL
    """

    with open('/Users/wumengling/PycharmProjects/customized_weibo/config/weibo_config.json', 'r') as weibo_config_file:
            weibo_config = load(weibo_config_file)
            oauth_client = Client(weibo_config['API_KEY'], weibo_config['API_SECRET'], weibo_config['REDIRECT_URI'],
                                  weibo_config['TOKEN'])
            oauth_client.post('favorites/create', id=mongo_obj_index_list[weibo_index])
