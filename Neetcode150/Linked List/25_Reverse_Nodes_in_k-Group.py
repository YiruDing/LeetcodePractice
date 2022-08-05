# 跑不了的 my solution:

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         result=ListNode()
#         tail=head=result

#         prev=None
#         count=k

#         while k:
#             nxt=head.next
#             cur=head
#             cur.next=prev
#             prev=nxt
#             count-=1
#             tail=tail.next
# ???   16行有問題：“NoneType" objects has no attribute "next"
# 怎麼改呢？
# 8/2 JM:不能一次做兩件事情，因為前一個group的頭，無法直接.next到下一個group的尾

#         head=head.next
#         count=k
#         return result.next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        groupPrev = result

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            # a.k.a groupNext?

            curr = groupPrev.next
            # ???
            # 每個group的頭

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            # the head of the next group
            groupPrev.next = kth
            groupPrev = tmp
        return result.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
