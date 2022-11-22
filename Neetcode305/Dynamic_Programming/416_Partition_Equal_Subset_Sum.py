class Solution:

    def canPartition(self, nums):
        t = sum(nums) / 2
        P = set([nums[0]])
        # 因為只要有一個值即可，這樣能省時間
        for x in nums[1:]:
            for y in list(P):
                # set儲存沒有按照順序喔，iterate應該比較麻煩...
                P.add(x + y)
        print('P :',P)
        # P : {1, 6, 11, 12, 17, 22}
        return t in P
    #   !!! 怎麼能據此確定nums的值可以對半分呢？


# My solution(to be fixed):
# 9/10 答案錯誤是因為必須考慮不同的排列組合，不能線性地疊加...
# 在解題過程中，重新命名nums.sort()出了問題，可以幫我看一下嗎？

    # def canPartition(self, nums):
    #     nums.sort()
    #     res1, res2 = 0, 0
    #     target = sum(nums) / 2

    #     l, r = 0, len(nums) - 1
    #     while l < r:
    #         if res1 < target:
    #             res1 += nums[l]
    #         elif res2 < target:
    #             res2 += nums[r]
    #         print('res1:', res1)
    #         print('res2:', res2)
    #         if res1 == target:
    #             return sum(nums[l + 1:]) == target
    #         elif res2 == target:
    #             return sum(nums[:r]) == target
    #         l += 1
    #         r -= 1
    #     return False

tmp = Solution()
tmp.canPartition([1, 5, 11, 5])