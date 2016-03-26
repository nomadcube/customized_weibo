def jaccard_similarity(a, b):
    one = set(a)
    other = set(b)
    return float(len(one.intersection(other))) / float(len(one.union(other)))
