# 1
class Solution(object):

    def getMinimumDifference(self, root):

        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)

        return fn(root, float('-inf'), float('inf'))


# 2
# 2/7 還沒搞懂
class Solution(object):

    def getMinimumDifference(self, root):
        nums = self.inorder(root)
        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(
            root.right) if root else []
