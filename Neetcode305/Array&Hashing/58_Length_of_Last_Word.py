class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        newS = s[::-1]
        count = 0
        for i in range(len(s)):
            if newS[i] == ' ':
                return count
            count += 1
        return count

    # 另解：
    #     def lengthOfLastWord(self, s: str) -> int:
    # s= s.rstrip()            # 2/16 本步驟可省略 removes spaces at the end
    # lst = s.split()          # gives a list of words by splitting at the spaces
    # return len(lst[-1])
