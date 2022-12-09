class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                # 12/8 不是root.left.val！！
                # 為何不能是 if node.val < left or node.val > right？因為這沒處理到left或right == root.val的狀況
                return False
            return (valid(node.left, left, node.val)
                    and valid(node.right, node.val, right))


# 7/31
# 這裡的left和right為float,而非node：所以不能用return(valid(node.left,left.val,node.val)and valid(node.right,node.val,right.val))？
# "float" object has no attribution 'val'

        return valid(root, float("-inf"), float("inf"))

    # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
