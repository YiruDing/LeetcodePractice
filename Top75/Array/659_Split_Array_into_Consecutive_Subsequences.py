# https://codeantenna.com/a/TL7l7GJhyv?fbclid=IwAR0zwtv6B3h_RkL1shiTLpFEPnPkgeGfcugOTjwwfoQPs_kZ5Z6vu92Nt0g

from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        expect = defaultdict(lambda x=1:(0,0))
        