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
        # 要加[],才能interate

        # 接下來加入的s3就會從index 1開始排起，有助於區別s1和s2的index...
        for (n, c) in zip(range(l3), s3):
            # 不是zip(l3, s3)
            # 這樣才能用到index
            b = set()
            for i in a:
                if i < l1 and s1[i] == c:
                    b.add(i + 1)
                # 如果s1[i] == c ,b.add(i + 1) ，不會跟下一行撞號
                if n - i < l2 and s2[n - i] == c:
                    # 不是elif
                    b.add(i)
                # n - i始於零減零，這樣就不會有漏掉的數字
                # 可是如果兩個都符合，不是應該兩個數字都加上去嗎？為何第40行沒加“0”呢？
                # 來來來，張開眼睛，b[0]沒符合啊！
            if len(b) == 0: return False
            print("b: ", b)
            a = b
            # 從新的index再去traverse
        return True


tmp = Solution()
tmp.isInterleave("aabcc", "dbbca", "aadbbcbcac")
# b:  {1}
# b:  {2}
# b:  {2}
# b:  {2, 3}
# b:  {2, 3}
# b:  {2, 4}
# b:  {3, 4}
# b:  {4, 5}
# b:  {4}
# b:  {5}

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
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]#正下方為True:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]#正右方為True:
                    dp[i][j] = True
        return dp[0][0]