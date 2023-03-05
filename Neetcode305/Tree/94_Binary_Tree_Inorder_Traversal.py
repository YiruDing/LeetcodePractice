# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive solution
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root: return None
            inorder(root.left)
            # 如果有左邊的值，就繼續走下去
            res.append(root.val)
            # 走到最左邊，儲值，然後再往上走
            inorder(root.right)
            # 不需要加res.append(root.val)，否則[1,3,2]會變成[1,3,3,2,2,1]

        inorder(root)
        return res


# Iterative solution
# Use stack to store the value,when a node has no left child,pop!
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            # 走到最左邊
            cur = stack.pop()
            res.append(cur.val)
            # 3/5 cur.val喔！
            cur = cur.right
            # append之後，往右一個node，再繼續往左走到底...
            # 基本上，他做的是上面inorder fn做的事情
        return res