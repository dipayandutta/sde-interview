from max_subarray import max_subarray_sum_size, max_subarray_sum_size_k

import pytest


@pytest.mark.parametrize("func", [max_subarray_sum_size, max_subarray_sum_size_k])
class TestMaxSubarraySum:
    def test_basic(self, func):
        assert func([4, 2, 1, -9, 8, 4, 3], 3) == 7

    def test_window_size_one(self, func):
        assert func([1, 3, -1, 7, 2], 1) == 3

    def test_window_equals_array_length(self, func):
        assert func([1, 2, 3], 3) == 6

    def test_all_negative(self, func):
        assert func([-5, -3, -8, -1, -4], 2) == -8

    def test_single_element(self, func):
        assert func([42], 1) == 42

    def test_window_at_start(self, func):
        assert func([9, 8, 1, 2, 3], 2) == 17

    def test_window_at_end(self, func):
        assert func([1, 2, 7, 9], 2) == 16

    def test_mixed_positive_negative(self, func):
        assert func([2, -1, 5, 6, -3, 4], 3) == 10
