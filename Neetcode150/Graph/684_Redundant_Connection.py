# Do Union Find by rank


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        # 0~len(edges)，共len(edges) + 1個parents 為什麼不是len(edges) 個呢？
        # e.gedges = [[1,2],[1,3],[2,3]]
        # 要讓index1的值剛好為1，必須這樣設定
        rank = [1] * (len(edges) + 1)

        def findParent(n):
            p = parent[n]

            while p != parent[p]:
                # 意味著parent[p]並非自己，而是可以往上找父母
                parent[p] = parent[parent[p]]
                p = parent[p]
                # 縮短路徑 path compression
            return p

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return False
            # 代表我們跑不下去 他們已經在同一棵樹下了/ they are already merged
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
