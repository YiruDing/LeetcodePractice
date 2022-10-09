from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)#Mapping the charChount to list of Anagrams

        for word in strs:
            count = [0] * 26#a...z

            for c in word:
                count[ord(c) - ord("a")] += 1
                # 用來記錄字母數一樣的word
                # 長得像這樣：
                # !! [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
                # Take the Unicode代碼點 以作為ｉｎｄｅｘ
                # https://vimsky.com/zh-tw/examples/usage/ord-function-python.html
            result[tuple(count)].append(word)
            # In Python,list can not be key,so we have to make it tuple

        return result.values()


# Another solution:
# https://www.youtube.com/watch?v=JG3vgcmHfso


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =  defaultdict(list)

        for word in strs:
            sk = "".join(sorted(word))
            # 8/23 sorted的字作key,word作value
            if sk in d:
                d[sk].append(word)
            else:
                d[sk] = [word]
        return d.values()
