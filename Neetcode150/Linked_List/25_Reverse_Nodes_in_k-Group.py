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
            # input [1,2,3,4,5] k=2 印出來長這樣
            # kth: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
            # kth: ListNode{val: 4, next: ListNode{val: 5, next: None}}
            # kth: None
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            # input [1,2,3,4,5] k=2 印出來長這樣
            # prev: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
            # prev: ListNode{val: 5, next: None}

            #為什麼prev的起始值跟groupNext一樣？?因為這樣才可以接續嗎？
            #143 Reorder List也有類似狀況，為什麼呢？

            curr = groupPrev.next
            # ???
            # 每個group的頭

            while curr != groupNext:
                # 處理在groupNext之前的node
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
