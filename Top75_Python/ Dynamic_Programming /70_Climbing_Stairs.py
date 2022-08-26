#  Fibonacci!!
# DFS bottom up


class Solution:

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            # Why is the range starts from 0 and go to n-2?
            # 因為間隔為n-1,有n-1步要處理
            temp = one
            one = one + two
            two = temp
        return one