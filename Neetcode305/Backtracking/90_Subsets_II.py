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
            # 3/11 在這裡我們可能加上duplicate
            subset.pop()

            # All subsets that don't include nums[i]

            #Avoit the duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                #  3/11 在這裡我們要跳過一個值（以及其duplicate）
                # 記得是確認 i + 1 < len(nums)
                i += 1
            backtrack(i + 1, subset)
            # indetation注意！ 還有 i + 1

        backtrack(0, [])
        return res
