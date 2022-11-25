class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(num, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for i in range(num, n + 1):
                cur.append(i)
                helper(i + 1, cur)
                cur.pop()

        helper(1, [])
        return res