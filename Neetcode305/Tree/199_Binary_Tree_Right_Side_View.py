# Either BFS or DFS works.
# However, according to Neetcode, BFS is simpler for this question...


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        # 等於
        # q = collections.deque()
        # q.append(root)

        while q:
            qlen = len(q)
            rightSide = None
            # 3/16 一次次歸零
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
                # 3/16 相較於102
                # 只取queue最後一個值，其餘捨棄

        return res

    # Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
