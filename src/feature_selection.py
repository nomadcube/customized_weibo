import numpy as np
import math


def pick_features(count_mat, lowest_percentile):
    origin_features, scores = inverse_doc_frequency(count_mat)
    low_threshold = np.percentile(scores, lowest_percentile)
    good_indices = np.where(scores >= low_threshold)
    return set(origin_features[good_indices])


def inverse_doc_frequency(count_mat):
    total_doc_count = count_mat.shape[0]
    features = np.array(count_mat.indices)
    feature, occurrence = _counting_occurrence(features)
    init_element = [math.log(float(total_doc_count) / occ) for occ in occurrence]
    return feature, init_element


def _counting_occurrence(arr):
    arr.sort()
    features = np.unique(arr)
    num_features = len(features)
    diff = np.ones(arr.shape, arr.dtype)
    diff[1:] = np.diff(arr)
    idx = np.where(diff > 0)[0]

    occurrence = np.ones(num_features)
    occurrence[0:num_features - 1] = np.diff(idx)
    occurrence[-1] = arr.shape[0] - np.diff(idx).sum()
    return features, occurrence
