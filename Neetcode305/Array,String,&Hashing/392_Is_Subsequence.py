# Bruce Force解法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):return False
        if len(s)==0 or not s or s==t:return True
        if len(s)==1 and s in t:return True
        idx=0
        count=len(s)
        for i in range(len(t)):
                if t[i]==s[idx] and idx<len(s):
                    idx+=1
                    count-=1
                if count==0:
                    return True
          
        return False
    
# Neetcode
    class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        
        while i<len(s)and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return True if i==len(s) else False
        
        