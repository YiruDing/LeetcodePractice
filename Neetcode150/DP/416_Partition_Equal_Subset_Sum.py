class Solution:

    # def canPartition(self, A):
    #     t = sum(A) / 2
    #     P = set([A[0]])
    #     # 因為只要有一個值即可，這樣能省時間
    #     for x in A[1:]:
    #         for y in list(P):
    #             # 記得嗎？set沒有按照順序喔，檢索應該比較麻煩...
    #             P.add(x + y)
    #     return t in P

# My solution(to be fixed):
# 9/10 我想，答案錯誤應該是是因為必須考慮不同的排列組合，不能線性地疊加...
# 在解題過程中，我print出問題，重新命名nums.sort()也出問題，可以幫我看一下嗎？
    def canPartition(self, nums: list[int]) -> bool:
# 在terminal用"Python3 416_Partition_Equal_Subset_Sum.py",得到如下回應：
# line 14, in Solution
# TypeError: 'type' object is not subscriptable
# StackOverFlow
        nums.sort()
        res1, res2 = 0, 0
        target = sum(nums) / 2

        l, r = 0, len(nums) - 1
        while l < r:
            if res1 < target:
                res1 += nums[l]
            elif res2 < target:
                res2 += nums[r]
            print('res1:', res1)
            print('res2:', res2)
            if res1 == target:
                return sum(nums[l + 1:]) == target
            elif res2 == target:
                return sum(nums[:r]) == target
            l += 1
            r -= 1
        return False


tmp = Solution
tmp.canPartition([1, 5, 11, 5])
