# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        count = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            lenQ = len(queue)
            level = []

            count += 1
            for i in range(lenQ):
                node = queue.popleft()
                print('node:', node)
                count += 1
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                print('level:', level)
                if count % 2:
                    res.append(level[::-1])
                else:
                    res.append(level)
        return res


# [3,9,20,null,null,15,7]

# node: TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
# level: [3]

# node: TreeNode{val: 9, left: None, right: None}

# node: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}
# level: [9, 20]
# node: None
# node: None

# node: TreeNode{val: 15, left: None, right: None}

# node: TreeNode{val: 7, left: None, right: None}
# level: [15, 7]

# node: None
# node: None
# node: None
# node: None
