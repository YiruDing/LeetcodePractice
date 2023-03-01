# 自己的解答
class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        stack = []
        list_s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])
                list_s[i] = 1

        for i in range(len(s)):
            if list_s[i] == 1:
                new_vowel = stack.pop()
                list_s[i] = new_vowel
        return ''.join(list_s)


# 超簡要解答
def reverseVowels(self, s):
    vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
    return re.sub('(?i)[aeiou]', lambda x: next(vowels), s)


# re.sub(pattern, repl, string[, count])
# https://blog.csdn.net/HHG20171226/article/details/101646130

# next(iterator, default)
# https://www.programiz.com/python-programming/methods/built-in/next

# (?i) makes it match case insensitive and
# https://stackoverflow.com/questions/22961535/what-does-i-and-in-this-regex-mean