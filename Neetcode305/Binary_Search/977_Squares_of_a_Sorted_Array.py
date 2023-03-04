# 1
class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])


# 2
class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None for _ in nums]
        # [None, None, None, None, None]
        # 這樣才可以收納値
        left, right = 0, len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left]**2
                left += 1
            else:
                result[index] = nums[right]**2
                right -= 1
        return result


# Neetcode
# Time: O(n), one pass using two pointers.
# Space: O(1), output array is not considered for space complexity.


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r - l] = left * left
                l += 1
            else:
                res[r - l] = right * right
                r -= 1
        return res