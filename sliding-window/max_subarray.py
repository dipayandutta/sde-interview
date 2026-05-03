def max_subarray_sum_size(nums, k):
    max_sum = float("-inf")
    for i in range(0, len(nums) - k + 1):
        current_sum = sum(nums[i : i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


result = max_subarray_sum_size([4, 2, 1, -9, 8, 4, 3], 3)
print(result)


def max_subarray_sum_size_k(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


result = max_subarray_sum_size([4, 2, 1, -9, 8, 4, 3], 3)

print(result)
