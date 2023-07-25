def knapsack_01(weights, values, capacity, n):
    if(n==0) or (capacity==0):
        result = 0
    elif (weights[n-1]>capacity):
        result = knapsack_01(weights, values, capacity, n-1)
    else:
        temp1 = knapsack_01(weights, values, capacity, n-1)
        temp2 = values[n-1] + knapsack_01(weights, values, capacity-weights[n-1], n-1)
        result = max(temp1, temp2)
    return result


# Example usage
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 10
n = len(w)

max_value = knapsack_01(w, v, c, n)
print("Maximum value:", max_value)