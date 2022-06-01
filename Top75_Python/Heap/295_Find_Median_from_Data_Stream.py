class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]
        # That's one way you have heap in Python
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)
        # Cause Python only impliment the MIN heap, 
        # !!!!but if we *-1, it will get the MAX heap by default
        if(self.small and self.large and (-1*self.small[0])>self.large[0]):
            # It means some of the value in S heap is greater than L heap
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
            
        if len(self.small)>len(self.large)+1:
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large)>len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        return(self.large[0]+ -1*self.small[0])/2