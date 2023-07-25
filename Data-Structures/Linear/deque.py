from collections import deque

# Create an empty deque
deq = deque()

# Add elements to the deque
deq.append(1)       # Add element to the right end
deq.appendleft(2)   # Add element to the left end

# Print the deque
print(deq)          # Output: deque([2, 1])

# Access elements from the deque
print(deq[0])       # Output: 2 (element at index 0)

# Remove elements from the deque
deq.pop()           # Remove element from the right end
deq.popleft()       # Remove element from the left end

# Print the deque after removal
print(deq)          # Output: deque([])

# Check if the deque is empty
print(len(deq) == 0)  # Output: True
