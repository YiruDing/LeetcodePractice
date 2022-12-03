class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS queue
        result = []
        queue = collections.deque()
        queue.append(root)
        # remember to append the root

        while queue:
            qLen = len(queue)
            # Since the queue is not empty,we got the number of queue...
            # To make sure we run one level at a time
            level = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    # 勿忘line17!
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                # To check the level is not empty
                # May29: Do it AFTER the for loop!!
                result.append(level)

        return result