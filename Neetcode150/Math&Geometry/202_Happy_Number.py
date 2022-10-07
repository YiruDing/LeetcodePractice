#Use set to make sure it would not be a endless loop

# 比較帥的解法
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1

# Neetcode 詳解
class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        
        while n not in visit:
            visit.add(n)
            n=self.sumOfSquares(n)
            
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self,n:int)->int:
            output=0
            
            while n:
                digit=n %10
                digit=digit**2
                output+=digit
                n=n//10
                
            return output
        