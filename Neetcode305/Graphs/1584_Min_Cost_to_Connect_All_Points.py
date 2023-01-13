# A problem related to minimun spanning tree(MST) or Prims
# https://web.ntnu.edu.tw/~algo/SpanningTree.html#3


# 普林演算法（Prim's algorithm）
# https://www.google.com/search?q=prims+%E6%BC%94%E7%AE%97%E6%B3%95&oq=prims&aqs=chrome.8.69i57j0i10l7j0i512l2.5884j0j7&sourceid=chrome&ie=UTF-8
# June 9 ...???? To be found out
class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i: [] for i in range(N)}  #i:list of [cost,node]
        # 1. Create the edges
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])


# 2. Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  #[cost,point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res

    # Jun 10 雖然不會重複，但如何確定這是最小值？？
    # minHeap ~~~
