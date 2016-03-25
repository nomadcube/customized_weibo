# coding=utf-8
import numpy as np


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
    由t时刻的前向概率递推计算t+1时刻的前向概率

    :param current_observation: int, 当前时刻的观测值
    :param last_forward_probability: N*1 array, 前一个时刻的前向概率
    :param a: matrix, 状态转移概率矩阵
    :param b: matrix, 观测概率矩阵
    :return: array, t+1时刻的前向概率向量
    """
    current_obs_b = np.array(b[:, current_observation].ravel())[0].reshape(last_forward_probability.shape)
    return np.array(last_forward_probability.transpose().dot(a).ravel())[0].reshape(current_obs_b.shape) * current_obs_b


def backward_probability_recursion(next_observation, next_backward_probability, a, b):
    """
    由t+1时刻的后向概率向量递推计算t时刻的后向概率向量

    :param next_observation: int, t+1时刻的观测值
    :param next_backward_probability: array, t+1时刻的后向概率向量
    :param a: matrix, 状态转移概率矩阵
    :param b: matrix, 观测概率矩阵
    :return: array, t时刻的后向概率向量
    """
    current_obs_b = np.array(b[:, next_observation].ravel())[0].reshape(next_backward_probability.shape)
    return np.array(a.dot(current_obs_b).ravel())[0].reshape(next_backward_probability.shape) * next_backward_probability


def likelihood(observation_sequence, a, b, p, algorithm="forward"):
    """
    用前向或后向算法计算观测序列O的似然值

    :param observation_sequence: list, 观测序列O
    :param a: matrix, 状态转移概率矩阵
    :param b: matrix, 观测概率矩阵
    :param p: array, 初始概率向量
    :param algorithm: str, "forward"表示选择前向算法，"backward"表示选择后向算法
    :return: float, 似然值
    """
    if algorithm == "forward":
        init_forward_prob = forward_probability_initiate(observation_sequence[0], b, p)
        for obs in observation_sequence[1:]:
            init_forward_prob = forward_probability_recursion(obs, init_forward_prob, a, b)
        return init_forward_prob.sum()
    if algorithm == "backward":
        init_backward = np.ones(init_forward.shape).reshape(p.shape) * p
        for obs in list(reversed(observation_sequence)):
            init_backward = backward_probability_recursion(obs, init_backward, a, b)
        return init_backward.sum()


if __name__ == '__main__':
    A = np.matrix([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]])
    B = np.matrix([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
    PI = np.array([0.2, 0.4, 0.4]).reshape((3, 1))
    observations = [0, 1, 0]
    init_forward = forward_probability_initiate(observations[0], B, PI)
    print init_forward
    second_forward = forward_probability_recursion(observations[1], init_forward, A, B)
    print second_forward
    init_backward = np.ones(init_forward.shape)
    print init_backward
    second_backward = backward_probability_recursion(observations[1], init_backward, A, B)
    print second_backward
    print likelihood(observations, A, B, PI)
    print likelihood(observations, A, B, PI, "backward")
