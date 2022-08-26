from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                # ！！！Ｍａｙ９待修理
                # Take the Unicode代碼點 以作為ｉｎｄｅｘ
                # https://vimsky.com/zh-tw/examples/usage/ord-function-python.html
            result[tuple(count)].append(s)
            # In Python,list can not be key,so we have to make it tuple

        return result.values()


# Another solution:
# https://www.youtube.com/watch?v=JG3vgcmHfso


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            sk = "".join(sorted(word))
            # 8/23 sorted的字作key,word作value
            if sk in d:
                d[sk].append(word)
            else:
                d[sk] = [word]
        return d.values()
