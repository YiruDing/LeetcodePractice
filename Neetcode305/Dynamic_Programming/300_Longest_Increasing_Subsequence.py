class Solution:
    # 3882 ms
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # From the end ...
            for j in range(i + 1, len(nums)):
                # Check every position after nums[i]
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

    # Most voted one
    # DP & sliding window
    # !! 212 ms
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                if tails[m] < x:
                    i = m + 1
                    # Check the right side 可以繼續往下...後面i+1表示長度可以加一
                else:
                    j = m
                    # Check the left side 回頭看看是否有可匹配的數值
            tails[i] = x
            size = max(i + 1, size)
            print('Check the size: ', size)
        return size


tmp = Solution()
tmp.lengthOfLIS([1, 2, 4, 3])

# Check the size:  1
# Check the size:  2
# Check the size:  3
# Check the size:  3