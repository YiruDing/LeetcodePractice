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
