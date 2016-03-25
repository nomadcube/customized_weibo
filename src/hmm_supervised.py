# coding=utf-8
import numpy as np


def hmm_supervised(obs_sequence, status_sequence):
    """
    隐马尔可夫模型的有监督学习
    已知实际观测序列和对应状态序列，估计模型参数：状态转移概率矩阵、观测概率矩阵、初始概率矩阵

    :param obs_sequence: list, 映射成整型后的观测序列
    :param status_sequence: list, 映射成整型后的状态序列
    :return: matrix 状态转移概率矩阵、matrix 观测概率矩阵、array 初始概率矩阵
    """
    obs_cnt = max(obs_sequence) + 1
    status_cnt = max(status_sequence) + 1

    pi = np.zeros((status_cnt, 1))
    for status in status_sequence:
        pi[status] = status_sequence.count(status) / float(len(status_sequence))

    a = np.zeros((status_cnt, status_cnt))
    for status_id in xrange(len(status_sequence) - 1):
        a[status_sequence[status_id]][status_sequence[status_id + 1]] += 1.0

    b = np.zeros((status_cnt, obs_cnt))
    for status_id in xrange(len(status_sequence)):
        b[status_sequence[status_id]][obs_sequence[status_id]] += 1.0

    return pi, (a.transpose()/a.sum(axis=1)).transpose(), (b.transpose()/b.sum(axis=1)).transpose()


if __name__ == '__main__':
    obs_seq = [0, 1, 0]
    status_seq = [1, 2, 0]
    print hmm_supervised(obs_seq, status_seq)
