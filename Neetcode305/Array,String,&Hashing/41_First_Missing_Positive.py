# https://www.cnblogs.com/grandyang/p/4395963.html
# 既然不能建立新的数组，
# 就充分利用既有list!
# 從i=1開始，遇到正數就＊-1，代表與以i為index的value已經存在，然後繼續往下走


# 3/8 過不了[1,2,0]...
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
            # 2/2 因為之後要讓每一個index和值掛鉤？
            if 1 <= val <= len(nums):
                # 3/8 記得這是限制 val 值
                # 縮小範圍，只列出可能的候選數目...這樣可能剔除過大的值，導致無值可找...所以在32行可以加一個回來
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # That means in this position we dont't get to store the value we want??
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        # 2/6其實這用其他負數也沒關係，重點只是用正/負值標註其index是否可用

        for i in range(1, len(nums) + 1):
            #
            if nums[i - 1] >= 0:
                # 2/2 i - 1代表的正整數不存在，故可做為答案
                # ！！3/8 不可為nums[i - 1] > 否則[1,2,0]就過不了了
                return i
        return len(nums) + 1


# Solution2
# https://www.youtube.com/watch?v=L1u-R_s2Mok
# 16:01


# 解三
# O(nlogn) time
def firstMissingPositive(self, nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res