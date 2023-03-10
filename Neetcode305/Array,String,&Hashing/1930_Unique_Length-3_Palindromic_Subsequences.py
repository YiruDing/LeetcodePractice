# T:O(26*n), S: O(n) by using the HashSet(key = (middle cahr, outside char))
# left = Set, right = HashMap


class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            # 從既有的開始算，這是跟左邊不一樣的地方
            for j in range(26):
                c = chr(ord('a') + j)
                # https://www.runoob.com/python/python-func-chr.html
                if c in left and c in right:
                    res.add((s[i], c))

            left.add(s[i])
            # Cause we could be introducing this newcharacter to the left portion
        return len(res)