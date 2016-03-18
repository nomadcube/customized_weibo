import json

weibo_config_path = '/Users/wumengling/PycharmProjects/customized_weibo/weibo_config.json'
API_KEY = '3794121772'
API_SECRET = 'c8a7307e9ebf356314242bf47e938b52'
REDIRECT_URI = 'http://127.0.0.1/library/Rweibo/doc/callback.html'
UID = '1860068802'
TOKEN = dict({'access_token': '2.00iresBC95klIEa5e72c689ehJSWAC',
              'remind_in': '157679999',
              'uid': '1860068802',
              'expires_at': 1601713686})

auth_config = dict()
auth_config['API_KEY'] = API_KEY
auth_config['API_SECRET'] = API_SECRET
auth_config['REDIRECT_URI'] = REDIRECT_URI
auth_config['UID'] = UID
auth_config['TOKEN'] = TOKEN

with open(weibo_config_path, 'w') as weibo_config:
    json.dump(auth_config, weibo_config)
    weibo_config.flush()
