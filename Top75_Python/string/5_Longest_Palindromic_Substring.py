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
            # extend the pointer outward
# even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        return result
    
    # Java 改良版
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        def palindrome(s,l,r):
            while l>=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s)):
            s1=palindrome(s,i,i)
            s2=palindrome(s,i,i+1)
            res=res if len(res)> len(s1) else s1
            res=res if len(res)> len(s2) else s2
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

