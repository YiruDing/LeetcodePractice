class Solution:

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                # skip the left/right character
                print('skipL:', skipL)
                print('skipR:', skipR)
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1
        return True

    # input "abakkaca"


#     skipL: akkac
# skipR: bakka