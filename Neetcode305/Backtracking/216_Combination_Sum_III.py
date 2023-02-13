# 官方解答
# https://leetcode.com/problems/combination-sum-iii/solutions/791715/combination-sum-iii/?orderBy=most_votes
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()
            # 2/13 也可以這樣寫：
            # for i in range(number + 1, 10):
                # path.append(i)
                # helper(target - i, path, i)
                # path.pop()

        backtrack(n, [], 0)

        return results