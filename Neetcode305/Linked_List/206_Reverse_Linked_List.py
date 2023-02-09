# 7/24
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # 問題：同樣是遍歷linked list, while head和while curr有何區別？
        while head:
            #這要用 while head
            # 否則用“while curr““會收到“ＡttributeError:'NoneType'object has no attribute 'next'”
            # 我了解為什麼用“while curr.next != None:” input[1,2,3,4,5]會得到結果[1],“while head.next != None:”會得到[4,3,2,1]，但'NoneType'object？
            # 找到最多人解答的討論串，但是看不懂：https://stackoverflow.com/questions/8949252/why-do-i-get-attributeerror-nonetype-object-has-no-attribute-something
            curr = head  # 2/9 儲head的值
            head = head.next  # 2/9 讓head的pointer移動
            curr.next = prev  # pointer轉向
            prev = curr  # 指定新的curr
            # 這個loop中的head
            # head: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
            # head: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
            # head: ListNode{val: 4, next: ListNode{val: 5, next: None}}
            # head: ListNode{val: 5, next: None}
            # head: None

            # 這要用 while curr
            #             next=curr.next #這樣curr之後就可以再接著做下去，不至於斷線
            #             curr.next=prev
            #             prev=curr
            #             curr=next
            print("curr:", curr)
# 這個loop中的curr
# curr: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# curr: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# curr: ListNode{val: 4, next: ListNode{val: 5, next: None}}
# curr: ListNode{val: 5, next: None}
# curr: None
        return prev


#             while head:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#             print("head:",head)
#             head: ListNode{val: 1, next: None}
# head: ListNode{val: 1, next: None}
# head: ListNode{val: 1, next: None}
# head: ListNode{val: 1, next: None}
# head: ListNode{val: 1, next: None}

#Some reference about declaimming LL
# https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode


# Solution 1(T O(n) M O(1))
class Solution:

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            # Before breaking the link,store the value
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    # new head


# Solution 1(T O(n) M O(n))
class Solution:

    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead