# Neetcode: It's like looking for the anagram


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        #initiate the counter，之後再移動window來確認

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            # 因為s1長度的s2已經放入s2Count中了
            if matches == 26: return True
            #  increment the window
            #  接下來right加字,左邊減字
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
#  decrement the window
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            left += 1
        return matches == 26


#
class Solution:

    def checkInclusion(self, p: str,
                       s: str) -> bool:  # renamed s1 to p, s2 to s
        cnt = Counter(p)
        print("cnt1:", cnt)
        # cnt1: Counter({'a': 1, 'b': 1})
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                # If number of characters `c` is more than our expectation
                #s1無此數或者該字母的數目多於預期（出現不該出現的字母），就馬上給他處理下去
                cnt[s[l]] += 1
                # 3/21
                # Slide left until cnt[c] == 0
                #！！！讓index從c之後開始
                print("cnt2:", cnt)
                l += 1
                print("left:", l)
                # input"ab" "aefghmab"
                # 印出如下：
                # (r=0時，cnt[a]=0.沒進入while loop)
                # cnt2: Counter({'a': 1, 'b': 1, 'e': -1})cnt[e]<0的loop...此時r=1
                # left: 1
                # 問題：為什麼後面沒有f或g小於0的key/value pair?
                # cnt2: Counter({'a': 1, 'b': 1, 'e': 0})此時r=2,l=1，所以s[l]＝＝e
                # left: 2
                # cnt2: Counter({'a': 1, 'b': 1, 'e': 0, 'f': 0})此時r=3,l=2,所以s[l]＝＝f,f值＋1=0
                # left: 3
                # cnt2: Counter({'a': 1, 'b': 1, 'e': 0, 'f': 0, 'g': 0})此時r=3,l=3,g值＋1=0
                # left: 4
                # cnt2: Counter({'a': 1, 'b': 1, 'e': 0, 'f': 0, 'g': 0, 'h': 0})
                # left: 5
                # cnt2: Counter({'a': 1, 'b': 1, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'm': 0})
                # left: 6
            if r - l + 1 == len(p):
                # If we already filled enough `p.length()` chars
                return True

        return False


# 3 solution
def checkInclusion(self, s1: str, s2: str) -> bool:
    cntr, w = Counter(s1), len(s1)

    for i in range(len(s2)):
        if s2[i] in cntr:
            cntr[s2[i]] -= 1
        if i >= w and s2[i - w] in cntr:
            cntr[s2[i - w]] += 1

        if all([cntr[i] == 0 for i in cntr]):  # see optimized code below
            return True

    return False
