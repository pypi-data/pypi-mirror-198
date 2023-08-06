# pylint: disable=missing-function-docstring
import unittest
import numpy as np
from numpy.testing import assert_array_equal
from microagg1d.main import optimal_univariate_microaggregation_1d, undo_argsort

def get_random_arr(seed, n):
    np.random.seed(seed)
    x = np.random.rand(100)
    order = np.argsort(x)
    x_sorted = x[order]
    return x, x_sorted, order


class RegularizedKmeans(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.arr = np.array([1, 1, 1, 1.1, 5, 5, 5])
        self.solutions = [
            [0, 1, 2, 3, 4, 5, 6],
            [0, 0, 1, 1, 2, 2, 2],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

    def test_undo_argsort_random(self):
        for seed in range(20):
            x, x_sorted, order = get_random_arr(seed, n=100)
            x_undone = undo_argsort(x_sorted, order)
            assert_array_equal(x, x_undone)

    def test_microagg_raises(self):
        with self.assertRaises(AssertionError):
            optimal_univariate_microaggregation_1d(np.random.rand(4,4), 1)

        with self.assertRaises(AssertionError):
            optimal_univariate_microaggregation_1d(self.arr, 0)

    def test_microagg(self):
        for k, solution in zip(range(1, len(self.arr)+1), self.solutions):
                result = optimal_univariate_microaggregation_1d(self.arr.copy(), k)
                np.testing.assert_array_equal(solution, result, f"k={k}")

    def test_example_usage(self):
        import microagg1d
        x = [5, 1, 1, 1.1, 5, 1, 5]
        k = 3

        clusters = microagg1d.optimal_univariate_microaggregation_1d(x, k)

        print(clusters)   # [1 0 0 0 1 0 1]
        np.testing.assert_array_equal(clusters, [1, 0, 0, 0, 1, 0, 1], f"k={k}")
if __name__ == '__main__':
    unittest.main()