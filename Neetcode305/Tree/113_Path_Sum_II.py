# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode],
                targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(root, path, sum):
            sum += root.val
            tmp = path + [root.val]
            if root.left:
                dfs(root.left, tmp, sum)
            #    not path, it's the tmp that should be the parameter
            if root.right:
                dfs(root.right, tmp, sum)
            if not root.left and not root.right and sum == targetSum:
                self.res.append(tmp)

        if not root: return []
        dfs(root, [], 0)

        return self.res
