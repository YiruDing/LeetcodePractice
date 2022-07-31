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
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res