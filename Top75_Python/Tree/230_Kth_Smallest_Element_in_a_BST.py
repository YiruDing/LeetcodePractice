# Another solution: https://www.youtube.com/watch?v=xMmceinGIa8


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder BAC
        stack = []
        while root or stack:
            # !!!
            # not "and"
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            # Go as far left as we can,adding value from the stack,and poping from the right when we need to
