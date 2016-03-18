import json

from src.data_collecting import craw_raw_data


class TestWeiboCrawler:
    def pytest_funcarg__weibo_config_path(self):
        return '/Users/wumengling/PycharmProjects/customized_weibo/config/weibo_config.json'

    def pytest_funcarg__serial_path(self):
        return '/Users/wumengling/PycharmProjects/customized_weibo/output/serializing.txt'

    def test_collect_data(self, weibo_config_path, serial_path):
        craw_raw_data(weibo_config_path, serial_path)
        with open(serial_path, 'r') as f:
            data = json.load(f)
        assert isinstance(data, dict)
        assert len(data) == 20
