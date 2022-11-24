class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right)


# Another way:
#  def sameTree(self, s, t):
#         if not s and not t:
#             return True

#         if s and t and s.val == t.val:
#             return (self.sameTree(s.left, t.left)) and (self.sameTree(
#                 s.right, t.right))
#         return False
