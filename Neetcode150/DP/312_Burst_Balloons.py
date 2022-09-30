# Neetcode solution code
# To be fixed...
class Solution:

    def maxCoins(self, nums):
        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get(
                        (pivot, right), 0)
                    cache[(left, right)] = max(coins,
                                               cache.get((left, right), 0))
                    print("cache:", cache, 'offset:', offset, 'left:', left,
                          'pivot:', pivot, 'right:', right)
        return cache.get((0, len(nums) - 1), 0)


tmp = Solution()
tmp.maxCoins([3, 1, 5, 8])

# cache: {(0, 2): 3} offset: 2 left: 0 pivot: 1 right: 2
# cache: {(0, 2): 3, (1, 3): 15} offset: 2 left: 1 pivot: 2 right: 3
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40} offset: 2 left: 2 pivot: 3 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40} offset: 2 left: 3 pivot: 4 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30} offset: 3 left: 0 pivot: 1 right: 3
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30} offset: 3 left: 0 pivot: 2 right: 3
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 64} offset: 3 left: 1 pivot: 2 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135} offset: 3 left: 1 pivot: 3 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 45} offset: 3 left: 2 pivot: 3 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48} offset: 3 left: 2 pivot: 4 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159} offset: 4 left: 0 pivot: 1 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159} offset: 4 left: 0 pivot: 2 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159} offset: 4 left: 0 pivot: 3 right: 4
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 51} offset: 4 left: 1 pivot: 2 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 70} offset: 4 left: 1 pivot: 3 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 159} offset: 4 left: 1 pivot: 4 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 159, (0, 5): 162} offset: 5 left: 0 pivot: 1 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 159, (0, 5): 162} offset: 5 left: 0 pivot: 2 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 159, (0, 5): 162} offset: 5 left: 0 pivot: 3 right: 5
# cache: {(0, 2): 3, (1, 3): 15, (2, 4): 40, (3, 5): 40, (0, 3): 30, (1, 4): 135, (2, 5): 48, (0, 4): 159, (1, 5): 159, (0, 5): 167} offset: 5 left: 0 pivot: 4 right: 5


# Neetcode video code
# To be fixed...
class Solution(object):

    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                # Deal with the left part and right part
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


# Leetcode 其他解
# https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # padding
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for i in range(left + 1, right):
                    # dp[left][right] = the maximum coins we get after bursting all the balloons between left and right (excluding left and right themselves)
                    dp[left][right] = max(
                        dp[left][right], dp[left][i] + dp[i][right] +
                        nums[left] * nums[i] * nums[right])
                    # maximum coins of bursting all the balloon on the left side of i
                    # maximum value of bursting all the balloon on the right side of i
                    # bursting balloon i last when left side and right side are gone
        return dp[0][
            n -
            1]  # since we pad nums on both sides with [1], it really covers the entire range of the original nums (remember boundaries are excluded)
