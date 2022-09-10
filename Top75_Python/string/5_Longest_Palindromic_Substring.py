class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        # odd length
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            print("first loop:", result)
            # extend the pointer outward

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            print("second loop:", result)
        return result


tmp = Solution()
tmp.longestPalindrome("sbabab der")

# 以下第一個字母為印出來的result值
# first loop: s(i=0 s[left]='s',s[right]='s'符合第一個while loop,但是s[left]<0,loop很快就結束了。)
# second loop: s(i=0 s[left]='s',s[right]='b'跳過第二個while loop)
# first loop: s(i=1 s[left]='b',s[right]='b'符合第一個while loop,還是沒能往外走。)
# second loop: s(i=1 s[left]='b',s[right]='a',跳過第二個while loop。)
# first loop: bab(i=2 s[left]='a',s[right]='a'符合第一個while loop,左右各往外走了一步。)
# second loop: bab(i=2 s[left]='a',s[right]='b',跳過第二個while loop。)
# first loop: babab(i=3 s[left]='b',s[right]='b'符合第一個while loop,左右各往外走了兩步。)
# second loop: babab(i=3 s[left]='b',s[right]='a',跳過第二個while loop。)
# first loop: babab(i=4 s[left]='a',s[right]='a'符合第一個while loop,左右各往外走了ㄧ步。但因為'bab'長度小於result,不能取代之)
# second loop: babab(i=4 s[left]='a',s[right]='b',跳過第二個while loop。)
# first loop: babab(i=5 s[left]='b',s[right]='b'符合第一個while loop,但不能往外走)
# second loop: babab(i=5 s[left]='b',s[right]='d',跳過第二個while loop。)
# first loop: babab(i=6 s[left]='d',s[right]='d'符合第一個while loop,但不能往外走)
# second loop: babab(i=6 s[left]='d',s[right]='e',跳過第二個while loop。)
# first loop: babab(i=7 s[left]='e',s[right]='e'符合第一個while loop,但不能往外走)
# second loop: babab(i=7 s[left]='e',s[right]='r',跳過第二個while loop。)
# first loop: babab(i=8 s[left]='r',s[right]='r'符合第一個while loop,但不能往外走)
# second loop: babab(i=8 s[left]='r',s[right]>len(s),loop很快就結束了。)


# Java 改良版
class Solution:

    def longestPalindrome(self, s: str) -> str:
        res = ""

        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res


# Java solution:
# class Solution {
#     public String longestPalindrome(String s) {
#         String res = "";
#         for (int i = 0; i < s.length(); i++) {
#             String s1 = palindrom(s, i, i);     // odd length palindroms
#             String s2 = palindrom(s, i, i+1);   // even length palindroms
#             // res = Math.max(res, s1, s2);
#             res = res.length() > s1.length() ? res : s1;
#             res = res.length() > s2.length() ? res : s2;
#         }
#         return res;
#     }

#     // find longest palindrom bewteen s[left] and s[right]
#     public String palindrom(String s, int left, int right) {
#         while (left >= 0 && right < s.length()
#                && s.charAt(left) == s.charAt(right)) {
#             left--; right++;
#         }
#         return s.substring(left+1, right);
#     }
# }
