# Mine
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ''
        reverse_list = []
        mark = {}
        for i in range(len(s)):
            if s[i].isalpha():
                reverse_list.append(s[i])
            else:
                mark[i] = s[i]
       

        
        for i in range(len(s)):
            if i in mark:
                res += mark[i]
            else:
                letter = reverse_list.pop()
                res += letter     

        return res
# 2 pointer
class Solution:
    def reverseOnlyLetters(self, S):
        S, i, j = list(S), 0, len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1
                # 2/14 上面這行別忘了！
        return "".join(S)
