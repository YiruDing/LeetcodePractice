import heapq

a = [7, 6, 5, 4, 3, 2, 1]
heapq.heapify(a)
print(a)
heapq.heappop(a)
print(a)
heapq.heappush(a, 1)
print(a)

b = [1, 2, 3, 4, 5, 6, 7]
heapq._heapify_max(b)
print(b)
heapq._heappop_max(b)
print(b)
heapq.heappush(b, 7)
print(b)