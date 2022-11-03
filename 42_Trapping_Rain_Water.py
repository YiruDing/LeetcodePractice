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
    
# https://leetcode.com/problems/trapping-rain-water/discuss/17575/Python-solutions-O(n)-space-and-O(1)-space
# The water we trapped depends on the left side and right side which has the max height,
# We keep the left side and right side until we find a higher side

class Solution:
# @param A, a list of integers
# @return an integer
def trap(self, arr):
    height, left, right, water = [], 0, 0, 0
    for i in arr:
        left = max(left, i)
        height.append(left)
    height.reverse()
    for n, i in enumerate(reversed(arr)):
        right = max(right, i)
        water += min(height[n], right) - i
    return water
# O(1)

class Solution:
# @param A, a list of integers
# @return an integer
 def trap(self, arr):
    left = right = water = 0
    i, j = 0, len(arr)-1
    while i <= j:
        left, right = max(left, arr[i]), max(right, arr[j])
        while i <= j and arr[i] <= left <= right:
            water += left - arr[i]
            i += 1
        while i <= j and arr[j] <= right <= left:
            water += right - arr[j]
            j -= 1
    return water

    
# JS解法(bruce force)
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

# JS解法(改良版)
# 1. Identify the pointer with the lesser value
# 2. Is this pointer value greater than or equal to max on that side
#   yes -> update max on that side
#   no -> get water for pointer, add to total
# 3. move pointer inwards
# 4. repeat for other pointer
#  */

const getTrappedRainwater = function(heights) {

  let left = 0, right = heights.length - 1, totalWater = 0, maxLeft = 0, maxRight = 0;
  
  while(left < right) {
    if(heights[left] <= heights[right]) {
      if(heights[left] >= maxLeft) { 
        maxLeft = heights[left]
      } else { 
        totalWater += maxLeft - heights[left];
      }
      left++;
    } else {
      if(heights[right] >= maxRight) {
          maxRight = heights[right];
      } else {
          totalWater += maxRight - heights[right];
      }
        
      right--;
    }
  }

  return totalWater;
}


console.log(getTrappedRainwater(elevationArray));