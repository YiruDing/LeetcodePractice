# ???
# To be debugged...

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder BAC
        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            # Go as far left as we can,adding value from the stack,and poping from the right when we need to
