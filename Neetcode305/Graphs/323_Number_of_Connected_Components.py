# Haven't submitted yet
# Leetcode Prime
# similar to 547
# Union Find


class Solution:

    def countComponents(self, n, edges) -> int:
        parent = [i for i in range(n)]
        # Each node will be the parent of themselves
        rank = [1] * n

        def find(n1):

            result = n1
            # c.f.684. Redundant Connection p = parent[n]
            while result != parent[result]:
                # Check if if's its own parent
                parent[result] = parent[parent[result]]
                # Make the linked list a little shorter
                # If there's no grandparent, the line above will basically do nothing
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
            print(rank)
            return 1

        # To indicate that we did perform a SUCCESSFUL union
        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
            # Every time we successfully union the node,we will decrement the result by one
        return result


# tmp = Solution()
# print(tmp.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
# (base) yi-ruding@teis-Air Graph % python3 1.py
# [2, 1, 1, 1, 1]
# [3, 1, 1, 1, 1]
# [3, 1, 1, 2, 1]
# 2
#減過三次union