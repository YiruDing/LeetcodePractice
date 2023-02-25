# https://leetcode.com/problems/range-sum-query-immutable/solutions/1406465/c-java-python-prefix-sum-clean-concise-o-1-space/?q=python&orderBy=most_votes
class NumArray:  # 68 ms, faster than 97.72%

    def __init__(self, nums: List[int]):
        self.preSum = nums  # pass by pointer!
        for i in range(len(nums) - 1):
            self.preSum[i + 1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.preSum[right]
        return self.preSum[right] - self.preSum[left - 1]


# 2
class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num

    def sumRange(self, left: int, right: int) -> int:
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[right + 1] - self.accu[left]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)