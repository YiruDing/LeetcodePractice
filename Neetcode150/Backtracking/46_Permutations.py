class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if (len(nums) == 1):
            return [nums.copy()]
        # Base case

        for i in range(len(nums)):
            n = nums.pop(0)
            # 0 as the index
            perms = self.permute(nums)
            # https://www.geeksforgeeks.org/python-pytorch-permute-method/

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            # Add multiple values to result
            nums.append(n)
            # Add to the end to the array
        return result


# The other solution:
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perm = []
#         def func(nums, ans):
#             if len(nums)==0:
#                 perm.append(ans)
#             for i in range(len(nums)):
#                     func(nums[:i]+nums[i+1:], ans+[nums[i]])
#         func(nums, [])
#         return perm

# 假設nums=[1,2,3],
# func([1,2,3],[])中，for loop會帶出
#                   func([2,3],[1])
#                   func([1,3],[2])
#                   func([1,2],[3])
# 第二輪
# func([2,3],[1])中，for loop會帶出
#                   func([3],[1,2])
#                   func([2],[1,3])
# func([1,3],[2])中，for loop會帶出
#                   func([3],[2,1])
#                   func([1],[2,3])
# func([1,2],[3])中，for loop會帶出
#                   func([2],[3,1])
#                   func([1],[3,2])
# 第三輪
# func([3],[1,2])中，for loop會帶出
#                   func([3],[1,2,3])
# func([2],[1,3])中，for loop會帶出
#                   func([2],[1,3,2])
# func([3],[2,1])中，for loop會帶出
#                   func([3],[2,1,3])
# func([1],[2,3])中，for loop會帶出
#                   func([1],[2,3,1])
# func([2],[3,1])中，for loop會帶出
#                   func([2],[3,1,2])
# func([1],[3,2])中，for loop會帶出
#                   func([1],[3,2,1])
# 第四輪，因為func中的num都變成[],以上六個值會被納入perm內，最後return
# 打完收工！
