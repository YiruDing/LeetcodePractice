# Leetcode 我比較看得懂的答案
class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = right_max = area = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    area += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    area += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return area


# Another solution
class Solution:

    def trap(self, height: List[int]) -> int:
        decreasingHeightStack, totalWaterTrapped = [], 0

        for i, v in enumerate(height):
            while len(decreasingHeightStack) > 0 and height[
                    decreasingHeightStack[-1]] < v:
                bottomHeight = height[decreasingHeightStack.pop()]
                if len(decreasingHeightStack) == 0:
                    break
                leftUpperIndex = decreasingHeightStack[-1]
                heightDiff = min(height[leftUpperIndex], v) - bottomHeight
                width = i - leftUpperIndex - 1
                totalWaterTrapped += heightDiff * width
            decreasingHeightStack.append(i)

        return totalWaterTrapped
    
# JS解法
 const elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

const getTrappedRainwater = function(heights) {
  let totalWater = 0;
  
  for(let p = 0; p < heights.length; p++) {
    let leftP = p, rightP = p, maxLeft = 0, maxRight = 0;

    while(leftP >= 0) {
      maxLeft = Math.max(maxLeft, heights[leftP]);
      leftP--;
    }

    while(rightP < heights.length) {
      maxRight = Math.max(maxRight, heights[rightP]);
      rightP++;
    }
    
    const currentWater = Math.min(maxLeft, maxRight) - heights[p];
    
    if(currentWater >= 0) {
      totalWater += currentWater;
    }
  }

  return totalWater;
}

console.log(getTrappedRainwater(elevationArray));