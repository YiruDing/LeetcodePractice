class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:
                result.append(cur.copy())
                # 2/9 這個很重要！
            if target < 0:
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
                prev = candidates[i]
                # !!!!!!!!!!!!!!!!!!!!!!!!!2/9 記得這行

        backtrack([], 0, target)
        return result
