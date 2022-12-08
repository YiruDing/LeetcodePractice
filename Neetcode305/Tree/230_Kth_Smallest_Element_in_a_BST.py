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
            # root左邊裝滿後，開始pop
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            # 左邊跑完，K還沒完，才需要走右邊
            # 12/6 不是 stack[0]
            
            root = root.right
            # Go as far left as we can,adding value from the stack,and poping from the right when we need to
