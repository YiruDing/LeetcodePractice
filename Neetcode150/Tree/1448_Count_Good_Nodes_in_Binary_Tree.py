# 2021微軟面試最愛


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        # Preorder traversal

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(node, node.val)


#待修的my solution
#       res=0

#         def dfs(r):
#             if r.left>r or r.right>r:
#                 res += 1
#             else:
#                 res += dfs(r.right)+dfs(r.left)

#             return res
