# Haven't submitted yet
# Leetcode Prime
# similar to 547
# Union Find


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        # Each node will be the parent of themselves
        rank = [1] * n

        def find(n1):
            # Check if if's its own parent
            result = n1

            while result != parent[result]:
                # Check if if's its own parent
                parent[result] = parent[parent[result]]
                # Make the linked list a little shorter
                # If there's no grand parent, the line above will basically do nothing
                # Path Compression. The idea is to flatten the tree when find() is called.
                # https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
                result = parent[result]
                # update the pointer to be its own parent
            return result

        def union(n1, n2):
            # Union/Merge the components together
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0


# We are not going to perform union
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                # p2 becomes the parent of p1
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        # To indicate that we did perform a SUCCESSFUL union

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
            # Every time we successfully union the node,we will decrement the result by one
        return result
