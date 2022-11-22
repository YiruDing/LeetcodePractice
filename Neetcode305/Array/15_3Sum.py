class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        # 和ＴwoSum不同，不需要管index

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            # 這兩行是在做什麼的？
            # n 值有重複，就跳過; 因為要確認[i - 1]的值，所以i 必須大於 0
            # 雖然這裡有在確認是否重複，但未更動pointer，因此下面的left還要再set the if staement and update the pointer.

            l, r = i + 1, len(nums) - 1
            while l < r:
                # 記得while loop!
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # line19-21是在res append之後，為了開啟下一階段而進行的準備

        return result