class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, total):
            # 可以收的先收起來
            if total == target:
                result.append(cur.copy())
                # So we can still keep the value that "cur" saved
                # And use it recursively
                return
                # !!不是return res!!
            # 踢掉沒可能的
            if i >= len(candidates) or total > target:
                return

            # 兩種可能：加（確認總和）或不加（往下走）。
            # 亦反映在cur上
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            #  +
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return result