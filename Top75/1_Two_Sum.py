# https://www.youtube.com/watch?v=KLlXCFG5TnA

# Python:
#  def twoSum(self, nums, target)

# Python3:
def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i
        return
    

