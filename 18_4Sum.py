# Leetcode官方解答
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    # 從頭開始跑，而且要確定數字不重複
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
                        # 在kSum內部自己append 結果
                        print("res:", res, "subset", subset)
            return res
# 11/3
# 假設 input為[-2,-1,0,0,1,2] target為0
# kSum(nums, target, 4)在上面紅字的迴圈，
# i==0
# 第一個是KSum([-1,0,0,1,2],2,3)，進入recursion
# 第二個是KSum([0,0,1,2],3,2)和KSum([0,1,2],2,2)，k==2
# KSum([0,0,1,2],3,2)進入twoSum,res append[1,2]。出了twoSum,res append[-1, 1, 2]，再往上走到第一個KSum，res append[-2, -1, 1, 2]
#KSum([0,1,2],2,2)進入twoSum,res append[0,2]。出了twoSum,res append[0, 0, 2]，再往上走到第一個KSum，res append[-2, 0, 0, 2]
# i==1
# 第一個是KSum([0,0,1,2],1,3)
# 第二個是KSum([0,1,2],1,2)和KSum([2],0,2)，k==2,
# 進入twoSum,res append[0,1]。出了twoSum,res append[0, 0,1]，再往上走到第一個KSum，res append[-1, 0, 0, 1]
# res: [[-1, 1, 2]] subset [1, 2]
# res: [[-1, 1, 2], [0, 0, 2]] subset [0, 2]
# res: [[-2, -1, 1, 2]] subset [-1, 1, 2]
# res: [[-2, -1, 1, 2], [-2, 0, 0, 2]] subset [0, 0, 2]
# res: [[0, 0, 1]] subset [0, 1]
# res: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]] subset [0, 0, 1]

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1

            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1
                                           and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4)


# 另解
def fourSum(self, nums, target):

    def findNsum(l, r, target, N, result, results):
        if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[
                r] * N:  # early termination
            return
        if N == 2:  # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:  # recursively reduce N
            for i in range(l, r + 1):
                if i == l or (i > l and nums[i - 1] != nums[i]):
                    findNsum(i + 1, r, target - nums[i], N - 1,
                             result + [nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums) - 1, target, 4, [], results)
    return results


# Base on 3Sum
class Solution(object):

    def threeSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1

        return results

    def fourSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeResult = self.threeSum(nums[i + 1:], target - nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results
