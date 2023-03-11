class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if (len(nums) == 1):
            return [nums.copy()]
        # 3/11 勿忘加上[]外框！ nums[:]會比較快！
        # Base case

        for i in range(len(nums)):
            n = nums.pop(0)
            # 0 as the index
            # 3/11 !!! 一定要寫0 !!!
            perms = self.permute(nums)
            # ！！3/11 現在有len(nums) - 1個數字，然後在這個步驟進行不同的排列組合
            # https://www.geeksforgeeks.org/python-pytorch-permute-method/

            for perm in perms:
                perm.append(n)
                # Append the 1st value we just removed
                # 3/11 把n加在尾巴
            result.extend(perms)
            # Add multiple values to result
            # 亦可作 result += perms
            nums.append(n)
            # Add to the end to the array
            # 3/11 把n加在尾巴
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
