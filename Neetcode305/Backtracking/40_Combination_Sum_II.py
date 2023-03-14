# 2/11 你值得更好的解答
class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)
            
# Neetcode

class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:
                result.append(cur.copy())
                # 2/9 2/10 這個很重要！後面line 50(應該是他吧＠＠)才可以繼續用
# 2/13 Why deep copy?
# JM:1.path.append(candidates[i]) 會用到喔...而且在不同層次的影響不同！
#     你寫一次nested recurrsion就明白了...
#    2. 再說，如果只是shallow copy, res append的referrence會因為之後的更動而被更動！那就不能正確呈現其值了

            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                    # 因為其他的值都是正數，所以這樣可以確保有重複狀況時，第一個if statement不用跑
                    # 又可以儲存之後的變數


# ???但是Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output當中可以有  [1,1,6],這又怎麼解釋呢？
# 8/14: 當你重新呼叫backtrack的時候，prev會被reset回“-1”啊！

                cur.append(candidates[i])
                # 2/9 這標示著新的recurrsion的開始
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                #    update prev
                # ！！！！！記得i + 1
                prev = candidates[i]
                # !!!!!!!!!!!!!!!!!!!!!!!!!2/9 記得這行

        backtrack([], 0, target)
        return result
