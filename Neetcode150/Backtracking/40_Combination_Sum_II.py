class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:
                result.append(cur.copy())
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    # 因為其他的值都是正數，所以這樣可以確保第一個if statement不用跑
                    # 又可以儲存之後的變數
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()

                prev = candidates[i]

        backtrack([], 0, target)
        return result
