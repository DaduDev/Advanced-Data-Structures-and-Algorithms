def find_max_min(arr, low, high):
    if low == high:
        # Base case: If there's only one element, it is both the maximum and minimum
        return arr[low], arr[low]

    elif low == high - 1:
        # Base case: If there are two elements, compare and return the maximum and minimum
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    else:
        # Divide the array into two halves
        mid = (low + high) // 2
        left_max, left_min = find_max_min(arr, low, mid)
        right_max, right_min = find_max_min(arr, mid + 1, high)

        # Compare the maximum and minimum from both halves
        return max(left_max, right_max), min(left_min, right_min)

# Example usage
arr = [3, 9, 1, 5, 0, 7, 11, 2, 4, 8, 6]

max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum element:", max_val)
print("Minimum element:", min_val)
