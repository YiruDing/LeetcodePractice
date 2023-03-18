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
        for n in nums:
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                if tails[m] < n:
                    # 3/18 雖然數值排列無規律，但因為要確認鄰居的值，還是可以用two points
                    i = m + 1
                    # Check the right side 可以繼續往下...後面i+1表示長度可以加一
                else:
                    j = m
                    # Check the left side 回頭看看是否有可匹配的數值
            tails[i] = n
            # 3/17 這行是做記錄，做為之後的基準
            size = max(i + 1, size)
            print('Check the size: ', size)
        return size


tmp = Solution()
tmp.lengthOfLIS([1, 2, 4, 3])

# Check the size:  1
# Check the size:  2
# Check the size:  3
# Check the size:  3