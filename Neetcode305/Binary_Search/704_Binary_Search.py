class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        
        while left<=right:
            index=(left+right)//2
            # Another way that will not overfloat:
            # index=left+(right-left)//2
            if nums[index]>target:
                right-=1
            elif nums[index]<target:
                left+=1
            else:
                return index
        return -1

# Mine...To be fixed
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         middle=len(nums)//2
        
#         while middle<len(nums) and middle >0:
#             if nums[middle]> target:
#                 middle-=1
#             elif nums[middle]<target:
#                 middle+=1
#             else:
#                 return middle
#         return -1