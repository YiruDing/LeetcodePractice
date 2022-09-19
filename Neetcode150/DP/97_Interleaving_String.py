# 用zip的解法
# https://leetcode.com/problems/interleaving-string/discuss/222406/Python-12-lines-easy-BFS


class Solution:

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = map(len, [s1, s2, s3])
        if l1 + l2 != l3: return False
        a = set([0])
        # 接下來加入的s3就會從index 1開始排起，有助於我們區別s1和s2的index...
        for (n, c) in zip(range(l3), s3):
            # 這樣才能用到index
            b = set()
            for i in a:
                if i < l1 and s1[i] == c: 
                    b.add(i + 1)
                # 如果s1[i] == c ,b.add(i + 1) ，不會跟下一行撞號
                if n - i < l2 and s2[n - i] == c: 
                    b.add(i)
                # 始於0-0，這樣就不會有漏掉的數字
            if len(b) == 0: return False
            a = b

# 9/18 待補
# Neetcode


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]