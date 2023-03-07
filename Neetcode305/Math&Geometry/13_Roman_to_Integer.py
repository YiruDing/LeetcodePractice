class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
# solution 2
# 1/19.. Why? 
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
*Note: The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.
# 哪裡錯了呢？
 dictionary = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if len(s) == 1:
            return dictionary[s]
        res = 0

        for i,w in enumerate(s):
            while i < len(s) - 1:
                if w == 'I' and (s[i +1] == 'V' or s[i+ 1] == 'X'):
                    res -= 1
                elif w == 'X' and (s[i +1] == 'L' or s[i+ 1] == 'C'):
                    res -= 10
                elif w == 'C' and (s[i +1] == 'D' or s[i+ 1] == 'M'):
                    res -= 100
                else:
                    res += dictionary[w]
            print('res:',res)
        return res     
