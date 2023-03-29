class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(s) < len(t): return ""

        char_counter = Counter(t)
        size = len(char_counter)
        window = {}
        have = 0
        left = 0
        resLen = float('inf')
        res = [-1, -1]

        for right, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in char_counter and char_counter[c] == window[c]:
                have += 1

            while have == size:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = min(resLen, len(s[left:right + 1]))
                window[s[left]] -= 1
                if s[left] in char_counter and window[s[left]] < char_counter[
                        s[left]]:
                    have -= 1
                # window[s[left]] -= 1
                # KeyError: 'N' 因為window[s[left]]可能不存在...那為何放到前面就可以呢？
                left += 1
        left, right = res
        return s[left:right + 1] if resLen != float('inf') else ''
