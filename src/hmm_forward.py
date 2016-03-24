# coding=utf-8
import numpy as np


def hmm_likelihood(observation_sequence, a, b, p):
    """
    已知隐马尔可夫模型的参数，用前向算法求特定观测序列的似然值

    :param observation_sequence: 观测序列，需要先将实际观测映射成整型索引值
    :param a: matrix, 状态转移概率矩阵
    :param b: matrix, 观测概率矩阵
    :param p: array, 初始概率向量
    :return: float, 观测序列obs的似然值
    """
    init_forward_prob = forward_probability_initiate(observation_sequence[0], b, p)
    for obs in observation_sequence[1:]:
        init_forward_prob = forward_probability_recursion(obs, init_forward_prob, a, b)
    return init_forward_prob.sum()


def forward_probability_initiate(init_observation, b, p):
    """
    计算各个观测取值对应的起始（即t=1时）的前向概率

    :param init_observation: int, 代表 t = 1 时的观测值
    :param b: N*M matrix, 观测概率矩阵
    :param p: N*1 array, 初始概率向量
    :return: N*1 array, 起始前向概率向量
    """
    return np.array(b[:, init_observation].ravel())[0].reshape(p.shape) * p


def forward_probability_recursion(current_observation, last_forward_probability, a, b):
    """
    由已知的t时刻的前向概率递推计算t+1时刻的前向概率

    :param current_observation: int, 当前时刻的观测值
    :param last_forward_probability: N*1 array, 前一个时刻的前向概率
    :param a: matrix, 状态转移概率矩阵
    :param b: matrix, 观测概率矩阵
    :param p: array, 初始概率向量
    :return: array, 由各个观测取值的t+1时刻的前向概率组成的向量
    """
    current_obs_b = np.array(b[:, current_observation].ravel())[0].reshape(last_forward_probability.shape)
    return np.array(last_forward_probability.transpose().dot(a).ravel())[0].reshape(current_obs_b.shape) * current_obs_b


if __name__ == '__main__':
    A = np.matrix([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]])
    B = np.matrix([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
    PI = np.array([0.2, 0.4, 0.4]).reshape((3, 1))
    observations = [0, 1, 0]
    print hmm_likelihood(observations, A, B, PI)
