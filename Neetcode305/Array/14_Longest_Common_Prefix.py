# 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
   
    # find shortest len so no index out of range error 
        lens = [len(str) for str in strs]
        min_len = min(lens)
        result = ''

        for i in range(1, min_len+1):
            prefix = strs[0][:i]
            # !!!strs[0][:i]!!!
            # 1/18: not strs[i][:j]
            for s in strs:             
                if s[:i] != prefix:
                    return result
            result = prefix
            # 不是這樣：
            #   result = prefix

        return result 
    dictionary = {I : 1 ; V : 5 ; X : 10 ; L : 50 ; }

# 2 
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            # https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)