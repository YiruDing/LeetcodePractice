#1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        result=0
        
        left=0
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            while(right-left+1)-max(count.values())>k:
                # Which means the situation that we are not able to make a change
                # !!max(count.values())
                count[s[left]]-=1
                # ！！！
                left+=1
            
            result=max(result,right-left+1)
        return result

#2        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        result=0
        
        left=0
        maxf=0
        
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            maxf=max(maxf,count[s[right]])
            while(right-left+1)-maxf>k:
                count[s[left]]-=1
                left+=1
            
            result=max(result,right-left+1)
        return result
        

        