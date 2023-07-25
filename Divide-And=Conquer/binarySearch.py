def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        else:
            return binary_search(arr, low, mid - 1, target)
    else:
        return -1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
