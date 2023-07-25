def is_subset_sum(set_nums, n, target_sum, subset=[]):
    if target_sum == 0:
        # Base case: The subset sum equals the target sum
        return True, subset
    if n == 0 or target_sum < 0:
        # Base case: No more elements to consider or target sum becomes negative
        return False, []

    # If the current element is greater than the target sum, skip it
    if set_nums[n - 1] > target_sum:
        return is_subset_sum(set_nums, n - 1, target_sum, subset)

    # Recursive case: include or exclude the current element in the subset
    include, subset_with = is_subset_sum(set_nums, n - 1, target_sum - set_nums[n - 1], subset + [set_nums[n - 1]])
    if include:
        return True, subset_with
    return is_subset_sum(set_nums, n - 1, target_sum, subset)


# Example usage
set_nums = [10, 7, 5, 18, 12, 20, 15]
target_sum = 35

is_possible, subset = is_subset_sum(set_nums, len(set_nums), target_sum)
if is_possible:
    print("Subset with sum equal to the target:")
    print(subset)
else:
    print("No subset found with the sum equal to the target.")
