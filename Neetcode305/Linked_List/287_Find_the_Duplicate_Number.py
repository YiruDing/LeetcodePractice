# hashset 可以有Ｏ(n),但題目要求O(1) space!!
# To apply the Floyd's agorithm to identify the beginning of the cycle
class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # find the intersection/ cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # move forward twice
            if slow == fast:
                break


# slow: 1
# fast: 3
# slow: 3
# fast: 4
# slow: 2
# fast: 4
# slow: 4
# fast: 4

# put the slow pointer in the intersection,the secod intersection will be the begining of the cycle
# 8:36
# the distance between the 1st intersection and the beginning of the cyle
#        ||
# the distance between the starting point and the begining of the cycle

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow