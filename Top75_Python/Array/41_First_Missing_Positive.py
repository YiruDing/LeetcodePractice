# May 19 還沒懂
# https://www.cnblogs.com/grandyang/p/4395963.html
# 既然不能建立新的数组，
# 那么只能覆盖原有数组，思路是把1放在数组第一个位置 nums[0]，2放在第二个位置 nums[1]，
# 即需要把 nums[i] 放在 nums[nums[i] - 1]上，遍历整个数组，
# 如果 nums[i] != i + 1, 而 nums[i] 为整数且不大于n，
# 另外 nums[i] 不等于 nums[nums[i] - 1] 的话，
# 将两者位置调换，如果不满足上述条件直接跳过，最后再遍历一遍数组，
# 如果对应位置上的数不正确则返回正确的数

# Solution1
class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        # Use the input array as the hashset

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            # Why modify the original value?
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # That means in this position we dont't get to store the value we want??
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        # So it would be easier for us to loop ...

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1

# Solution2
# https://www.youtube.com/watch?v=L1u-R_s2Mok
# 16:01