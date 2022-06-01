from cmath import inf


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # To modify it easily, he made it a list

        # return the max path sum without slplit
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            #    Update the result with asplit(the global value)
            result[0] = max(result[0], root.val + leftMax + rightMax)

            # Return the value without a split
            return root.val + max(leftMax, rightMax)


# I can also return max(result[0],root.val+max(leftMax,rightMax))

        dfs(root)
        return result[0]

    # https://www.youtube.com/watch?v=9ZNky1wqNUw
    # 7:21


class Solution:

    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return -sys.maxint
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)

    def maxPathSum(self, root):
        self.ans = -sys.maxint
        self._maxPathSum(root)
        return self.ans


# Other solution:
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/1445709/124-binary-tree-maximum-path-sum-python-solution