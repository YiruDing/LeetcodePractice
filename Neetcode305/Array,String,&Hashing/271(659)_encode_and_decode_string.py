# 以下兩個解答，皆以["Hello","World"]為例
class Codec:

    def encode(self, strs):
        ans = ''.join('%d:' % len(s) + s for s in strs)
        print('!!', ans)
        # !! 5:Hello5:World
        # It's used for formatting strings.
        # %s acts a placeholder for a string
        # %d acts as a placeholder for a number.
        return ans

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            # string.find(value, start, end)
            # find(）找不到值的時候會return -1
            # The find() method is almost the same as the index() method,
            # the only difference is that the index() method raises an exception if the value is not found. (See example below)
            # index()找不到值的話，會這樣...
            # Traceback (most recent call last):
            #   File "demo_ref_string_find_vs_index.py", line 4 in <module>
            #     print(txt.index("q"))
            # ValueError: substring not found

            i = j + 1 + int(s[i:j])
            strs.append(s[j + 1:i])
        return strs


# https://www.lintcode.com/problem/659/
class Codec:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s


# res: 5#Hello
# res: 5#Hello5#World
        return res

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            # 當j=="#",while 斷開後，append其值。
            # 3/9 因為可能超過個位數，必須這樣操作
            length = int(str[i:j])
            # i始於原點，j是其後的“＃”，所以str[i:j]就是“5#Hello”的5!!!
            # length: 5
            res.append(str[j + 1:j + 1 + length])
            # 3/9 j在delimiter（＃）的位置，所以要加一
            i = j + 1 + length
        return res