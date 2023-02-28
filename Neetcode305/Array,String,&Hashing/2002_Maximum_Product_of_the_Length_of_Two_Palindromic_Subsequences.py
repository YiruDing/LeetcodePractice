# Neetcode T:Ｏ（2^n）S:O(2^n)^2
# Transform the binary representation to the string to the palindrome it presents
#HashMap[key = bitmask,str 的二元]
# value 為palindrome的長度


class Solution:

    def maxPalindrome(self, s):
        N, pali = len(s), {}  #bitmask: length

        for mask in range(1, 1 << N):  # 1 << N == 2 ** N
            # 2/27: 1 是哪裡來的？
            subseq = ''
            for i in range(N):
                if mask & (1 << i):
                    # 2/27 不是 and 喔！
                    # Check if it include the charaater at this position
                    subseq += s[i]  #right to left
                    # You can also try this to add to the right side: N - i - 1
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:  # !!! disjoint
                    res = max(res, pali[m1] * pali[m2])
            return res


# 1 time/space 皆為最佳解
# 2/27 為何是用加的？？
class Solution:

    def maxPalindrome(self, s):
        # 2/27 為何是用加的？？
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 從右下角開始往回加...
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    def maxProduct(self, s: str) -> int:
        ans = 1
        for i in range(1, 2**len(s) + 1):
            # 2**len(s) 每一個位置都有兩個選擇？
            first = ''
            remain = ''
            for j in range(len(s)):
                if i & (2**j):
                    # 2/27 ?
                    first += s[j]
                else:
                    remain += s[j]
            if first != first[::-1] or not remain:
                continue
            ans = max(ans, len(first) * self.maxPalindrome(remain))
        return ans


# 2 bitmask 比較好處理disjoin
# Neetcode: so that we can use the 'and' operation to determine
# if two subsequences happen to be disjoint
# bitmask https://zhuanlan.zhihu.com/p/148827170
class Solution:

    def maxProduct(self, s: str) -> int:
        # n <= 12, which means the search space is small
        n = len(s)
        arr = []

        for mask in range(1, 1 << n):
            subseq = ''
            for i in range(n):
                # convert the bitmask to the actual subsequence
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))

        arr.sort(key=lambda x: x[1], reverse=True)
        result = 1
        for i in range(len(arr)):
            mask1, len1 = arr[i]
            # break early
            if len1**2 < result: break
            for j in range(i + 1, len(arr)):
                mask2, len2 = arr[j]
                # disjoint
                if mask1 & mask2 == 0 and len1 * len2 > result:
                    result = len1 * len2
                    break

        return result