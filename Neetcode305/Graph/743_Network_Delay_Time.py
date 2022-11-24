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

        minHeap = [(0, k)]  #時間,起始點
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1


# Most voted solution
# Heap
class Solution:

    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1


# Queue
class Solution:

    def networkDelayTime(self, times, N, K):
        t = [0] + [float("inf")] * N
        # Python特別的語法...會變成[0,float("inf",float("inf"...]
        #   因為起始點為1~N的整數，墊一個0能讓之後的index跟起始點的數值相通，操作方便很多
        # >>> [0] + [1]
        # [0, 1]
        # >>> [0] * 10
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # >>> [0] + [float("inf")] * 10

        graph = collections.defaultdict(list)
        q = collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                #node為起始點，node值跟index值一樣
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1


# ParthoBiswas007
#  Uses simple DFS - Accepted
class Solution(object):

    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float("inf") for node in range(1, N + 1)}
        # 此range的設定範圍，也是要讓起始點和index對應
        self.DFS(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float("inf") else -1

    def DFS(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[
                node]:  # signal already reached to this node. so no need to explore for this node
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            # sorted(graph[node]:已經照時間短到長排列了
            self.DFS(graph, distance, neighbour, elapsedTimeSoFar + time)


# """