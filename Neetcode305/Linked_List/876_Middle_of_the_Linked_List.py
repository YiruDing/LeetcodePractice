class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    # 2/14 !!!不是return slow.next!!!!
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head

        while cur:
            arr.append(cur)
            cur = cur.next
        
        middle = len(arr) // 2
        return arr[middle]