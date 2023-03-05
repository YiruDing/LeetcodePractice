# DFS
def minDepth1(self, root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# BFS
def minDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    # 3/5 不是([root,1])喔！
    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
