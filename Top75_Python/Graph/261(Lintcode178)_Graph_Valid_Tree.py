# Haven't run the code yet
# After get the prime

# https://www.lintcode.com/problem/178/

# check if there's no cycle(not going to be add again in visit) and every node is connected to other(visit set)


def validTree(self, n, edges):
    # n is the number of nodes
    # edges are some pairs of nodes(undirected)
    if not n:
        return True

    adj = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()

    def dfs(i, prev):
        if i in visit:
            return False

        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            # skip
            if not dfs(j, i):
                # ??Not connected???
                return False
        return True

    # Didn't detect a loop

    return dfs(0, -1) and n == len(visit)
