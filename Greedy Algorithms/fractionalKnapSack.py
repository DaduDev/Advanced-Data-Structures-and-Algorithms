def fractional_knapsack(w, v, c):
    items = list(zip(w, v))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    max_value = 0

    for weight, value in items:
        if c >= weight:
            max_value += value
            c -= weight
        else:
            max_value += (value / weight) * c
            break

    return max_value


# Example usage
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 5

max_value = fractional_knapsack(w, v, c)
print("Maximum value:", max_value)