class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        # 把所有可能的值，當作一個array，便於找出最適合的答案
        result = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if h >= hours:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1

        return result


# More Good Binary Search Problems
# Here are some similar binary search problems.
# Also find more explanations.
# Good luck and have fun.

# Kth Missing Positive Number
# Minimum Number of Days to Make m Bouquets
# Find the Smallest Divisor Given a Threshold
# Divide Chocolate
# Capacity To Ship Packages In N Days
# Koko Eating Bananas
# Minimize Max Distance to Gas Station
# Split Array Largest Sum

# Why can't I do this???
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left,right=1,max(piles)
#         result=right

#         while left<=right:
#             k=(left+right)//2
#             for p in piles:
#                 h -= math.ceil(p/k)
# Ｏct10 這樣無法好好調整k的值
# 而且我們不該去動parameter,這樣以後就無法再次使用了
#             if h>0:
#                 result=min(result,k)
#                 right=k-1
#             else:
#                 left=k+1

#         return result
