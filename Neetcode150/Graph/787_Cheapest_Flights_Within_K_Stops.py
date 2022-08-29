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
    
# another possible solution(to be fixed...)
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
            for u,v,p in flights:
            edges[u].append((v,p))
        
        minHeap=[(0,src)]
        visit=set()
        p=0
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            p=max(p,w1)
            
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return p 
