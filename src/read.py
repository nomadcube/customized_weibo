# coding=utf-8
def base_read(file_name):
    """
    将一个文档集读成list of list类型
    文档集中各个文档对应一个list, list的元素是该文档中的所有映射后的词条

    :param file_name: 文档集所在文件名
    :return: list, 包含所有的文档
    """
    all_doc = list()
    with open(file_name, "r") as f:
        for line in f:
            all_doc.append(line.strip().split(" "))
    return all_doc


if __name__ == '__main__':
    ad = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")
    print len(ad)
