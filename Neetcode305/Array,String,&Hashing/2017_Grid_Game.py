class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        # prefix
        length = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        for i in range(1, length):
            preRow1[i] += preRow1[i - 1]
            preRow2[i] += preRow2[i - 1]

        res = float('inf')
        for i in range(length):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res


# Neetcode 另解
# Time: O(n) Space: O(1)


class Solution(object):

    def gridGame(self, grid):
        result = float("inf")
        left, right = 0, sum(grid[0])

        for a, b in zip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result