import src.recommendation.Rocchio


class TestRecommendation:
    def pytest_funcarg__lhs_word_vec(self):
        return ['pytest', 'funcarg', 'lhs', 'word', 'vec']

    def pytest_funcarg__rhs_word_vec(self):
        return ['pytest', 'funcarg', 'rhs', 'word', 'vec']

    def pytest_funcarg__lhs_word_vec_numeric(self):
        return [0, 3, 4]

    def pytest_funcarg__rhs_word_vec_numeric(self):
        return [1, 3, 2]

    def pytest_funcarg__candidate_list(self):
        return [[1, 3, 4], [2, 3, 4], [1, 3, 2]]

    def pytest_funcarg__pos_feedback(self):
        return [[1, 3, 4], [2, 3, 4], [1, 3, 2]]

    def pytest_funcarg__neg_feedback(self):
        return [[4, 4, 1], [2, 0, -1], [11, 32, 2]]

    def test_discard(self, lhs_word_vec, rhs_word_vec):
        assert src.recommendation.similarity.similarity(lhs_word_vec, rhs_word_vec) == float(4) / float(6)

    def test_euro(self, lhs_word_vec_numeric, rhs_word_vec_numeric):
        assert src.recommendation.similarity.similarity(lhs_word_vec_numeric, rhs_word_vec_numeric, 'euro') == pow(5, 0.5)

    def test_k_nearest_brute_force(self, lhs_word_vec_numeric, candidate_list):
        res = src.recommendation.k_nearest.k_nearest(lhs_word_vec_numeric, candidate_list, 2)
        assert len(res) == 2
        assert res == [[1, 3, 4], [2, 3, 4]]

    def test_centroid(self, neg_feedback):
        res = src.recommendation.Rocchio.centroid(neg_feedback)
        assert res[0] == (17.0 / 3.0)
        assert res[1] == 12
        assert res[2] == 2.0 / 3.0

    def test_rocchio(self, lhs_word_vec_numeric, pos_feedback, neg_feedback):
        res = src.recommendation.Rocchio.rocchio_update(lhs_word_vec_numeric, pos_feedback, neg_feedback, 1.0, 2.0, 0.5)
        # assert res[0] == (-1) * (1.0 / 6.0)
        assert res[1] == 3
        assert res[2] == 31.0 / 3.0
