# coding=utf-8
from io import open
from scipy.sparse import coo_matrix, csr_matrix
from array import array


def base_read(file_name):
    """
    将一个文档集读成list of list类型
    文档集中各个文档对应一个list, list的元素是该文档中的所有映射后的词条

    :param file_name: 文档集所在文件名
    :return: list, 包含所有的文档
    """
    real_id = list()
    all_doc = list()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            id, doc = line.strip().split("||")
            all_doc.append(doc.split(" "))
            real_id.append(id)
    return real_id, all_doc


def read_sparse(file_name):
    """
    将一个文档集读成稀疏矩阵
    所有项作为特征，项在特定一个文档中的频次作为特征取值

    :param file_name: str, 文档集对应文件名
    :return: coo_matrix
    """
    real_id = list()
    row_index = array('I')
    col_index = array('I')
    element = array('f')
    with open(file_name, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f):
            id, doc = line.strip().split("||")
            real_id.append(id)
            words = doc.split(" ")
            for one_word in words:
                row_index.append(int(line_no))
                col_index.append(int(one_word))
                element.append(words.count(one_word))
    return real_id, coo_matrix((element, (row_index, col_index)), dtype="float")

if __name__ == '__main__':
    from feature_selection import inverse_doc_frequency, pick_features
    ad = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")
    print len(ad)
    mat = read_sparse("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")[1]
    mat = csr_matrix(mat)
    print mat.shape
    print len(pick_features(mat, 10))
