class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        # Backtrack dfs
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # 也可以寫作return result

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result