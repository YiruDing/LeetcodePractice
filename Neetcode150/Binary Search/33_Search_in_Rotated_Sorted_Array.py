class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid


# 我未成功的嘗試
#             if nums[mid]>=target and target > nums[right] :
# #                 左半邊，往右
#                 right=mid-1
#             elif nums[mid]<target and target < nums[left] :
# #                 右半邊，往左
#                 left=mid+1
#             elif nums[mid]>target and target < nums[right] :
#                 left=mid+1
# #               右半邊，往右
#             elif nums[mid]<target and target < nums[right] :
#                 right=mid-1

            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1