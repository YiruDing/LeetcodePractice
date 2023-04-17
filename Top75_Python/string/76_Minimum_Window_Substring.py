from json.encoder import INFINITY


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            # 0 is the default value

        have = 0
        need = len(countT)
        result = [-1, -1]
        resultLen = float('infinity')
        left = 0

        for right in range(len(s)):
            count = s[right]
            window[count] = 1 + window.get(count, 0)

            if count in countT and window[count] == countT[count]:
                # 因為可能有duplicates，所以要確認window[count] == countT[count]
                have += 1

            while have == need:
                # Update/Trim the result
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1
                window[s[left]] -= 1
                # 4/17 下面是要去確認window[s[left]]的狀況，只有window[s[left]] - 1， 才能符合window[s[left]] < countT[s[left]]的條件:
                # remove the left most to shrink the window
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left:right + 1] if resultLen != float('infinity') else ""
