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


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         result=0
#         if not root:
#             return result

#         if root.left or root.right:
#             return 1+max(diameterOfBinaryTree(self,root.left),diameterOfBinaryTree(self,root.right))