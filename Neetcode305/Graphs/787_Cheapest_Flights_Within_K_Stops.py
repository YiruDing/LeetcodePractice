# Bellman-Ford algorithm
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    # 意味無法reach this source node
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            # June9：pay attention on the indentation
        return -1 if prices[dst] == float('inf') else prices[dst]


# Priority Queue Solution
class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1


#Another BFS


class Solution1(object):

    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        q = collections.deque()
        min_price = float('inf')

        for u, v, w in flights:
            graph[u].append((w, v))
        q.append((src, 0, 0))
        while q:
            city, stops, price = q.popleft()
            if city == dst:
                min_price = min(min_price, price)
                continue

            if stops <= K and price <= min_price:
                for price_to_nei, nei in graph[city]:
                    q.append((nei, stops + 1, price + price_to_nei))

        return min_price if min_price != float('inf') else -1


# Python Dijkstra
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/267200/python-dijkstra/?q=python&orderBy=most_relevant
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
# n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# graph:[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# s: 0 graph[s]: {1: 100}
# s: 1 graph[s]: {2: 100}
# s: 2 graph[s]: {0: 100}
# s: 1 graph[s]: {2: 100, 3: 600}
# s: 2 graph[s]: {0: 100, 3: 200}
        pq = [(0, src, k + 1)]
        # 價錢，出發地，轉機數
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w + dw, y, k - 1))
        return -1


# Python heapq doesn't support update heap node's weight. But if you implement your own heap structure and support that function, you can maintain a n-size heap and time complexity is O((m + n)logn). m is number of edges and n is number of nodes. And it can be improved to O(m + nlogn) with a Fibonacci heap where a delete min costs logn but an update cost costs constant time.