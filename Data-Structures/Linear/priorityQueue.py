import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]

# Example usage
pq = PriorityQueue()
pq.push('Task 1', 5)
pq.push('Task 2', 1)
pq.push('Task 3', 3)

while not pq.is_empty():
    print("Next task:", pq.pop())
