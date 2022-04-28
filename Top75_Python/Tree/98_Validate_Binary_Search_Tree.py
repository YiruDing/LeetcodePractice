from operator import truediv


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val)
                    and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
