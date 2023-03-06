# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            # 3/6 TreeNode(值)
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        # 3/6 記得這一行

        return helper(0, len(nums) - 1)
