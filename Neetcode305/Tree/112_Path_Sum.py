# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 題目不是 binary search tree喔！因為沒有按照大小排，必得遍歷所有node

# https://www.youtube.com/watch?v=LSKQyOz_P8I
# Neetcode 6:14 Time Complexity O(n), Space complexity will becth height of the tree,若是a balanced tree 可為O(log n)，最差是O(n)

# Inorder DFS
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curSum):
            # 因為這方式是慢慢加起每個node的值，所以須另起一function
            if not node:
                return False

            curSum += node.val

            if not node.left and not node.right:
                return curSum == targetSum

            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)
    
# Recursion

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == sum:
                
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    # !!!12/1 .val!!!
    # 1/31 OR!!
    