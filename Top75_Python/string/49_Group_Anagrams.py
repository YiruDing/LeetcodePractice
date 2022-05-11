from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                # ！！！Ｍａｙ９待修理
                # Take the Unicode代碼點 以作為ｉｎｄｅｘ
                # https://vimsky.com/zh-tw/examples/usage/ord-function-python.html
            result[tuple(count)].append(s)

        return result.values()