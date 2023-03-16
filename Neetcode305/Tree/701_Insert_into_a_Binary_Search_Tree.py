# My solution 待修
class Solution:

    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val > val and root.left.val < val and not root.left.right:
            root.left.right = val
        if root.val < val and root.right.val > val and not root.right.left:
            root.right.left = val

        l = self.insertIntoBST(root.left, val)
        r = self.insertIntoBST(root.right, val)

        return root