# Another solution: https://www.youtube.com/watch?v=xMmceinGIa8


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder BAC
        stack = []
        while root or stack:
            # !!!
            # 3/16 3/27 not "and"
            while root:
                stack.append(root)
                # 3/16 為何不是append(cur.val)?比較：Leetcode 102
                # 3/27 JM:這是append node，之後會使用到
                root = root.left
            # root左邊裝滿後，開始pop
            root = stack.pop()
            # 3/21 之後要往右走，亦得從每個node去走...
            k -= 1
            if k == 0:
                return root.val
            # 左邊跑完，K還沒完，才需要走右邊
            # 12/6 不是 stack[0]

            root = root.right
            # Go as far left as we can,adding value from the stack,and poping from the right when we need to
