# https://leetcode.com/problems/linked-list-in-binary-tree/solutions/524881/python-recursive-solution-o-n-l-time/?q=python&orderBy=most_votes
# Solution 1: Brute DFS
def isSubPath(self, head, root):

    def dfs(head, root):
        if not head: return True
        if not root: return False
        # 一定是先確認head 再處理root!
        # ＪＭ：窮舉之後，再統整
        
        return root.val == head.val and (dfs(head.next, root.left)
                                         or dfs(head.next, root.right))
  
    if not head: return True
    if not root: return False
    return dfs(head, root) or self.isSubPath(
        head, root.left) or self.isSubPath(head, root.right)
      # 提供不同的開頭...


# Solution 2: DP
class Solution(object):

    def isSubPath(self, head, root):
        A, dp = [head.val], [0]
        i = 0
        node = head.next
        while node:
            while i and node.val != A[i]:
                i = dp[i - 1]
            i += node.val == A[i]
            A.append(node.val)
            dp.append(i)
            node = node.next

        def dfs(root, i):
            if not root: return False
            while i and root.val != A[i]:
                i = dp[i - 1]
            i += root.val == A[i]
            return i == len(dp) or dfs(root.left, i) or dfs(root.right, i)

        return dfs(root, 0)