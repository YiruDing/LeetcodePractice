# preOrder(ABC) the 1st value is the root node
#               the 2nd       is the root for the left part
# inorder(BAC)  Every value before the root is going to the left
#                          after                           right
# Every value of the tree is unique


class Solution:

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
