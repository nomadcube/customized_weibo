# coding=utf-8
import numpy as np

from src.hmm.hmm_likelihood import forward_probability_initiate


def single_status_probability(forward_prob, backward_prob):
    """
    已知模型参数、观测序列，求时刻t下各状态的概率
    由特定时刻t下的前向概率向量和后向概率向量计算

    :param forward_prob: 时刻t的前向概率向量
    :param backward_prob: 时刻t的后向概率向量
    :return: 时刻t的各状态出现概率向量
    """
    if forward_prob.shape != backward_prob.shape:
        raise ValueError("Shape of forward and backward probability must be the same.")
    each_status_score = forward_prob * backward_prob
    return each_status_score / each_status_score.sum()


def adjacent_status_probability(current_forward_prob, next_backward_prob, next_observation, a, b):
    """
    由t时刻的前向概率向量和t+1时刻的后向概率向量，计算得出"t时刻在状态i且t+1时刻在状态j"的概率

    :param current_forward_prob: t时刻的前向概率向量
    :param next_backward_prob: t+1时刻的后向概率向量
    :param next_observation: t+1时刻的观测值
    :param a: 状态转移概率矩阵
    :param b: 观测概率矩阵
    :return: N*N 矩阵
    """
    ab = np.array(a) * (np.array(b[:, next_observation].ravel())[0])
    alpha_ab = (ab.transpose() * current_forward_prob).transpose()
    each_score = alpha_ab * next_backward_prob.reshape(alpha_ab[0].shape)
    return each_score / each_score.sum()


if __name__ == '__main__':
    A = np.matrix([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]])
    B = np.matrix([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
    PI = np.array([0.2, 0.4, 0.4]).reshape((3, 1))
    observations = [0, 1, 0]
    init_forward = forward_probability_initiate(observations[0], B, PI)
    print init_forward
    init_backward = np.ones(init_forward.shape)
    print single_status_probability(init_forward, init_backward)
    print adjacent_status_probability(init_forward, init_backward, 0, A, B)
