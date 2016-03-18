from similarity import similarity


def k_nearest(query, candidate_list, k, search_algorithm='brute_force', dist_algorithm='discard'):
    """
    For the query, find k nearest neighbor in candidates, using the given algorithm.
    O(kn) complexity.
    """
    if search_algorithm == 'brute_force':
        """Find k neighbor using selection sort."""
        res = dict()
        candidate_count = len(candidate_list)
        for i in range(k):
            smallest_distance = similarity(query, candidate_list[i], dist_algorithm)
            neighbor_index = i
            for candidate_index in range(i, candidate_count):
                simi = similarity(query, candidate_list[candidate_index], dist_algorithm)
                if simi > smallest_distance:
                    smallest_distance = simi
                    neighbor_index = candidate_index
            res[''.join(candidate_list[neighbor_index])] = smallest_distance
        return res
