# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Ｔ：Ｏ（n）
class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return

            res.append('(')
            res.append(str(root.val))

            if not root.left and root.right:
                # 如果left是None 而right不是...
                res.append('()')
            preorder(root.left)
            preorder(root.right)

            res.append(')')
            # 3/6 記得這行

        preorder(root)
        return ''.join(res)[1:-1]