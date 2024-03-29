# 8/4 取值時，只能split一次...一魚兩吃，maxPathSum可以讓我們取得階段性的值(return的部分)和result
# 8/1 為什麼跑不了？


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # To modify it easily, he made it a list.But we can totally do "self.result=root.val"

        # return the max path sum without slplit
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            # What if all the values are negtive?
            # ????Shouldn't it start with leftMax = max(leftMax, float('-inf'))???
            rightMax = max(rightMax, 0)
            #    Update the result with a split(the global value)
            result[0] = max(result[0], root.val + leftMax + rightMax)

            # Return the value without a split
            return root.val + max(leftMax, rightMax)

# I can also return max(result[0],root.val+max(leftMax,rightMax))

        dfs(root)
        return result[0]

    # https://www.youtube.com/watch?v=9ZNky1wqNUw
    # 7:21


# My unsolved solution
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res=root.val

#         def seek(node):
#             if not node:
#                 return res
#             if node.left.val>0 and node.left.val>node.right.val:
#                 res+=node.left.val
#                 node=node.left
#             elif node.right.val >0 and node.left.val<node.right.val:
#                 res+=node.right.val
#                 node=node.right
#             elif node.left.val<0 and node.right.val<0:
#                 res=0
#                 seek(node.left)
#                 seek(node.right)

#         seek(root)
#         return res


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


# another solution:
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/1445709/124-binary-tree-maximum-path-sum-python-solution
