# 4/18:
# To Be debuged...

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists) >1:
            mergedLists=[]
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists
        return lists[0]
        
        
    def mergeList(self,L1,L2):    
        result = ListNode()
        tail = result
        
        while L1 and L2:
            if L1.val < L2.val:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next
        
        if L1:
            tail.next = L1
        elif L2:
            tail.next = L2
            
        return tail.next
        
        