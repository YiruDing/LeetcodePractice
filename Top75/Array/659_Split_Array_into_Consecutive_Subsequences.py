# https://codeantenna.com/a/TL7l7GJhyv?fbclid=IwAR0zwtv6B3h_RkL1shiTLpFEPnPkgeGfcugOTjwwfoQPs_kZ5Z6vu92Nt0g

# 1
from collections import defaultdict
# https://docs.python.org/3/library/collections.html

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        expect = defaultdict(lambda x=1:(0,0))
        # ??? the value of x=1 is (0,0)
        n=len(nums)
        if n==0:
            return True
        i=0
        while i<n:
            b=i
            if b>0 and nums[b]!=nums[b-1]+1:
                # nums[b] can't be the next value behind nums[b-1]
                if expect[nums[b-1]][1]+expect[nums[b-1]-1][1]!=0:
                    #??? Why should expect[nums[b-1]][1]+expect[nums[b-1]-1][1]=0?????
                    return False
            while i<n and nums[i]==nums[b]:
                i+=1
            cnt = i-b
            unsatisfy=expect[nums[b]-1][1]+expect[nums[b]-2][1]
            if cnt< unsatisfy:
                return False
            expect[nums[b]] = (cnt,max(0,cnt-expect[nums[b]-1][0]))
            return expect[nums[-1]-1][1]+ expect[nums[-1]][1]==0
        
# 3
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq = Counter(nums)
        need = Counter()
        for x in nums:
            if freq[x]==0:
                continue
            if need[x]>0:
                need[x] -= 1
                need[x+1] += 1
                # You will need x+1
            elif freq[x+1]>0 and freq[x+2]>0:
                freq[x+1] -= 1
                freq[x+2] -= 1
                need[x+3] += 1
                # you will need x+3
            else:
                return False
            freq[x] -= 1
            # ?????
        return True