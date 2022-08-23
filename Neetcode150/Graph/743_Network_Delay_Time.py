# Dijkstra's algorithm - the shortest path graph algorithm
class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k is the starting point
        edges = collections.defaultdict(list)
        # 当key不存在时，返回的是list的默认值[ ]
        # The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
        # https://www.geeksforgeeks.org/defaultdict-in-python/
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # pop出來不是v,w嗎？為何此處倒過來寫呢？因為除了第一個已設定好的值之外，後面都是把v和w倒過來存的
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
