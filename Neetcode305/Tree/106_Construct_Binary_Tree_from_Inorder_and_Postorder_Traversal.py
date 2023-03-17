class Solution:

    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        # 下面的postorder已經是pop掉的了
        inorderIndex = inorder.index(root.val)  # Line A

        root.right = self.buildTree(inorder[inorderIndex + 1:],
                                    postorder)  # Line B
        root.left = self.buildTree(inorder[:inorderIndex], postorder)  # Line C

        return root