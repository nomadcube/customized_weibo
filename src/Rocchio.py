from numpy import array


def centroid(arr):
    """Calculate centroid of the given array."""
    m = len(arr)
    arr_sum = array(arr[0])
    for i in range(1, m):
        arr_sum += array(arr[i])
    return arr_sum / float(m)


def rocchio_update(query, pos_feedback, neg_feedback, alpha, beta, gamma):
    """Update the query with pos_feedback and neg_feedback, with weight alpha, beta and gamma."""

    query_arr = array(query)
    pos_centroid = centroid(pos_feedback)
    neg_centroid = centroid(neg_feedback)
    return alpha * query_arr + beta * pos_centroid - gamma * neg_centroid
