class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        #會花O(n) time 反正這本來就是要花的

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


# 下面這種寫法是不行的...
# 因為如果input 為[1,2,3]
# 正解為 -1，但此處答案會為1
class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        half = sum(nums) // 2
        lSum = 0
        for i in range(len(nums)):
            lSum += nums[i]
            if lSum >= half:
                # lSum > half 一樣不行喔！
                return i

        return -1