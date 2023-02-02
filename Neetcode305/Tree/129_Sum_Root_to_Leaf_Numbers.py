# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sumNumbers(self, root):  # DFS recursively
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, path):

        if root:
            # 記得這一條！
            if not root.left and not root.right:
                path = path * 10 + root.val
                self.res += path
            self.dfs(root.left, path * 10 + root.val)
            self.dfs(root.right, path * 10 + root.val)
