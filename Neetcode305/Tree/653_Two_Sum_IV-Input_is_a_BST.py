# Solution 1: HashSet


# Note: this solution doesn't take the advantage that our Binary Tree is a Binary Search Tree.
# 3/25 因為解答可能出現是不相鄰的兩個node的和，有必要使用set儲值
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def dfs(root, seen):
            if root == None: return False
            complement = k - root.val
            if complement in seen: return True
            seen.add(root.val)
            # 3/25 是root.val而非complement!!
            return dfs(root.left, seen) or dfs(root.right, seen)

        return dfs(root, set())

    # 類似解法
    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False


# Solution 2: Stack (Interviewer expects this solution)


# By using the idea from 173. Binary Search Tree Iterator problem
class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:

        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False


# Solution 3: Python yield
# 有趣但是還沒懂


# With the support of yield and yield from in Python, we can just simple dfs inOrder and dfs inOrderReversed then we can fire elements in order and in reversed order.
# Read more about yield at: What does the “yield” keyword do?
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inOrder(root):
            if root:
                yield from inOrder(root.left)
                yield root.val
                yield from inOrder(root.right)

        def inOrderReversed(root):
            if root:
                yield from inOrderReversed(root.right)
                yield root.val
                yield from inOrderReversed(root.left)

        leftGenerator = inOrder(root)
        rightGenerator = inOrderReversed(root)

        left, right = next(leftGenerator), next(rightGenerator)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = next(leftGenerator)
            else:
                right = next(rightGenerator)
        return False