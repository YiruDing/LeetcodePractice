class Solution:

    def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                # Update the leftMax so the res could add a positive number
                # 先update,之後才不避處理負數的問題
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
# 一個簡單粗暴的解法
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        res = 0
        for i in range(1, n-1):
            if height[i] < left[i] and height[i] < right[i]:
                res += min(left[i], right[i]) - height[i]
        return res
    
# 另解
# 10/11還沒看懂...
#        __     __rightUpper2
# leftUpper |  _|
#           |_| rightUpper1
#            ^
#       lowerHeight
# rightUpper1 traps 1 x 1(width x height) units of water.
# rightUpper2 traps 2 x 1(width x height) units of water.
# Stack store decreasing heights that can be possible “leftUpper” .
# Whenever we meet a “rightUpper”, we should accumulate water trapped.

# How much water is trapped because of the rightUpper?
# water trapped = width * height
# The width of water trapped depends on distance from “leftUpper” to “rightUpper”, so we save index rather than height
# The height of water trapped depends on min(leftUpper, rightUpper) - lowerHeight.

class Solution:
    def trap(self, height: List[int]) -> int:
        decreasingHeightStack, totalWaterTrapped = [], 0
        
        for i, v in enumerate(height):
            while len(decreasingHeightStack) > 0 and height[decreasingHeightStack[-1]] < v:
                bottomHeight = height[decreasingHeightStack.pop()]
                print("bottomHeight:",bottomHeight)
                if len(decreasingHeightStack) == 0:
                    break
                leftUpperIndex = decreasingHeightStack[-1]
                print("leftUpperIndex:",leftUpperIndex)
                heightDiff = min(height[leftUpperIndex], v) - bottomHeight
                width = i - leftUpperIndex - 1
                totalWaterTrapped += heightDiff * width
                print("totalWaterTrapped:",totalWaterTrapped)
            decreasingHeightStack.append(i)
            
        return totalWaterTrapped
    
# [0,1,0,2,1,0,1,3,2,1,2,1]
# bottomHeight: 0
# bottomHeight: 0
# leftUpperIndex: 1
# totalWaterTrapped: 1
# bottomHeight: 1
# bottomHeight: 0
# leftUpperIndex: 4
# totalWaterTrapped: 2
# bottomHeight: 1
# leftUpperIndex: 4
# totalWaterTrapped: 2
# bottomHeight: 1
# leftUpperIndex: 3
# totalWaterTrapped: 5
# bottomHeight: 2
# bottomHeight: 1
# leftUpperIndex: 8
# totalWaterTrapped: 6