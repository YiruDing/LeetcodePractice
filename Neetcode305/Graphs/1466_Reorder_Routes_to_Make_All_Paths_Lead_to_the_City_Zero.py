class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal neighbors, edges, visit, changes
            # https://blog.csdn.net/qq_34240459/article/details/105218757
            # https://blog.csdn.net/HappyRocking/article/details/80115241
            # 在local scoup 改變global scoup 的變量

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)

        visit.add(0)
        dfs(0)
        return changes