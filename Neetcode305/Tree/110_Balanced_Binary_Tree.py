class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            #   因為這樣可以控制在可調整的範圍

            return [balanced, 1 + max(left[1], right[1])]


# max(left[1], right[1]而非 dfs(root.left)[1], dfs(root.right)[1]

        return dfs(root)[0]
