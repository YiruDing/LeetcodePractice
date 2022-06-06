# https://www.youtube.com/watch?v=KLlXCFG5TnA

# Python:
#  def twoSum(self, nums, target)


# Python3:
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # list? List?
        # See the disscution in https://stackoverflow.com/questions/52629265/static-typing-in-python3-list-vs-list

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

    #     June 3 :Why would I need to return again here??
