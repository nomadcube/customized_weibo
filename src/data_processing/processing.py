# coding=utf-8

from hdfs import InsecureClient
import json


def chinese_shingle(hdfs_serial_path):
    """Read data from hdfs serial path and shingle it to list with unicode string as element."""

    res = []
    client = InsecureClient('http://127.0.0.1:50070')
    with client.read(hdfs_serial_path, encoding='utf-8') as reader:
        data = reader.read()
        data_dict = json.loads(data)
        for line in data_dict.keys():
            res.append([word for word in line.strip('\n')])
    return res


if __name__ == '__main__':
    res = chinese_shingle('weibo_4.json')
    print(res)
    print(type(res))
    print(len(res))
    print(res[0])
    print(''.join(res[0]))
