def quick_sort(arr):
	length = len(arr)
	if(length <= 1):
		return arr
	else:
		pivot = arr.pop()

	items_greater = []
	items_lower = []

	for items in arr:
		if(items > pivot):
			items_greater.append(items)
		else:
			items_lower.append(items)
	return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)



arr = list(map(int, input("Enter the elements seperated by space : ").split(" ")))
print(quick_sort(arr))