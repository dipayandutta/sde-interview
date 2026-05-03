def sliding_window_product(nums, k):
    if k > len(nums):
        return None

    # Step 1: initial window product
    product = 1
    for i in range(k):
        product *= nums[i]

    print(f"Window {nums[0:k]} -> {product}")

    # Step 2: slide the window
    for i in range(k, len(nums)):
        if nums[i - k] == 0:
            # fallback: recompute window (important edge case)
            product = 1
            for j in range(i - k + 1, i + 1):
                product *= nums[j]
        else:
            product = product // nums[i - k]  # remove outgoing
            product = product * nums[i]  # add incoming

        print(f"Window {nums[i-k+1:i+1]} -> {product}")


nums = [1, 4, 1, 6, -3, 3, -5, 2, 26]
k = 4
sliding_window_product(nums, k)
