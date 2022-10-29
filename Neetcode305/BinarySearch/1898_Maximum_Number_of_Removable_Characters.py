class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        pCount = collections.Counter(p)
        rCount = {}
        res = 0

        for i in range(len(removable)):
            rCount[removable[i]] = 1 + rCount.get(removable[i], 0)

        for c in pCount:
            if pCount[c] < rCount[c]:
                res += rCount[c] - pCount[c]
        return res


    # Neetcode answer
class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def isSubseq(s, subseq):
            i1, i2 = 0, 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    # 已經被移走，或是未找到標的物
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1

            return i2 == len(subseq)

        # 如果i2可以走到最後，就代表他是subseq

        res = 0
        l, r = 0, len(removable) - 1
        # Binary search on removable
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m + 1])
            if isSubseq(s, p):
                res = max(res, m + 1)
                # 數字而非index，所以要加一。也可以寫作len(removed)
                l = m + 1
            else:
                r = m - 1
        return res
