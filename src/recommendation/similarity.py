from numpy import array


def similarity(lhs_word_vector, rhs_word_vector, measurement='discard'):
    """
    Take two word vector as input. Calculate the distance between them using measurement.

    :param lhs_word_vector: list
    :param rhs_word_vector: list
    :return: float
    """
    if measurement == 'discard':
        lhs_set = set(lhs_word_vector)
        rhs_set = set(rhs_word_vector)
        return float(len(lhs_set.intersection(rhs_set))) / float(len(lhs_set.union(rhs_set)))

    if measurement == 'euro':
        try:
            if len(lhs_word_vector) != len(rhs_word_vector):
                raise ValueError('Length of two word vector must be the same.')
            lhs_array = array(lhs_word_vector)
            rhs_array = array(rhs_word_vector)
            return 1.0 / 1 + pow(sum(pow(lhs_array - rhs_array, 2)), 0.5)
        except ValueError:
            print('Length of two word vector must be the same.')
