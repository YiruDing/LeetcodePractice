# 1
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
            # 剔除掉沒可能的
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


#2
class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        res = []

        def helper(idx, path, t):
            if t == target:
                res.append(path.copy())
                return
            if t > target or idx >= len(candidates):
                return

            helper(idx, path + [candidates[idx]], t + candidates[idx])
            # 因為每一個數都可以無限疊加，所以在這個可能性中，idx可以維持原位
            helper(idx + 1, path, t)
            # 亦可忽略此處的值，徑直往前

        helper(0, [], 0)
        return res