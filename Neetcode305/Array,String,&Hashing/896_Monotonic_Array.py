#  1
# https://leetcode.com/problems/monotonic-array/solutions/165889/c-java-python-one-pass-o-n/?q=python&orderBy=most_votes
 def isMonotonic(self, A):
        return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}
    # mp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
    
# 2
# https://leetcode.com/problems/monotonic-array/solutions/165960/python-solution-easy-to-understand/?q=python&orderBy=most_votes
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        n = len(A)
        if n <= 2: return True
				
        isGreat = False
        isLess = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                isGreat = True
            if A[i - 1] < A[i]:
                isLess = True

            if isGreat and isLess:
                return False

        return True