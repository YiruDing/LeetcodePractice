# 待debug


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = []

        def dfs(root, path, sum):
            currentSum = sum - root.val

            tmp = collections.deque(path)
            tmp.append(root.val)
            if currentSum < 0:
                tmp.popleft()

            if root.left:
                dfs(root.left, tmp, currentSum)
            if root.right:
                dfs(root.right, tmp, currentSum)
            if currentSum == 0:
                res.append(tmp)

        if not root: return []
        dfs(root, [], targetSum)
        return len(res)


# https://leetcode.com/problems/path-sum-iii/solutions/170367/python-solution/?q=python&orderBy=most_votes
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def dfs(root, prevSum, sum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - sum in rec:
                count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, sum)
            count += dfs(root.right, currSum, sum)
            rec[currSum] -= 1
            return count

        rec = {0: 1}
        return dfs(root, 0, sum)
    
# https://leetcode.com/problems/path-sum-iii/solutions/91892/python-solution-with-detailed-explanation/
# Brute Force Solution

The simplest solution is to traverse each node (preorder traversal) and then find all paths which sum to the target using this node as root.
The worst case complexity for this method is N^2.
If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2). This is the merge sort recurrence and suggests NlgN.
class SolutionBruteForce(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result
