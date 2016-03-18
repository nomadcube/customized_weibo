from src.data_processing import processing


def main(hdfs_serial_path='weibo_4.json'):
    original_docs = processing.chinese_shingle(hdfs_serial_path)
    print(''.join(original_docs[0]))
    recommend_res = src.recommendation.k_nearest.k_nearest(original_docs[0], original_docs[1:], 1)
    print(recommend_res)
    print(recommend_res.keys()[0])


if __name__ == '__main__':
    main()
