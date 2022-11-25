class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # 11/25 要sort!!

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            # All subsets that includes nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]

            #Avoit the duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                # 不是nums[i - 1] == nums[i]??因為已經append過，再處理沒意義了，只能處理未來的那個數字
                i += 1
            backtrack(i + 1, subset)
            # indetation注意！ 還有 i + 1

        backtrack(0, [])
        return res
