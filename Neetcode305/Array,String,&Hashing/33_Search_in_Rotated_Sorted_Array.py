class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # 3/28 意味他們同屬於左半邊..等號因此該放這裡唷！
                if target > nums[mid] or target < nums[left]:
                    # 3/27 都是 or!!
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1