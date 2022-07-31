class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return result[0]


# 另外一個解法：
# ？？？為什麼res必須在function diameterOfBinaryTree之外？？？？？？
# https://maxming0.github.io/2020/04/26/Diameter-of-Binary-Tree/
# class Solution:
#     res = 0
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         def dfs(root):
#             if not root:
#                 return 0
#             l = dfs(root.left)
#             r = dfs(root.right)
#             self.res = max(self.res, l + r)
#             return max(l, r) + 1

#         if not root:
#             return 0
#         dfs(root)
#         return self.res

# ???"name"diameterOfBinaryTree"is not defined"
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         result=0
#         if not root:
#             return result

#         if root.left or root.right:
#             return 1+max(diameterOfBinaryTree(self,root.left),diameterOfBinaryTree(self,root.right))