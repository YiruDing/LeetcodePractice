# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# XXXXX Use hashSet 較耗記憶體 XXXXX
# O（1）space solution O(m+n) time
# Use list for our advantage...跑兩次後，能找到intersection
class Solution:

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1