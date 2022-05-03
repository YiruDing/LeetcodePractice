
# Solution 1(T O(n) M O(1))
class Solution:
    def reverseList(self, head):
        prev,curr = None, head
        
        while curr:
            nxt = curr.next
            # Before breaking the link,store the value 
            curr.next=prev
            prev=curr
            curr = nxt
        return prev
    # new head
    
# Solution 1(T O(n) M O(n))
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        
        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        
        return newHead