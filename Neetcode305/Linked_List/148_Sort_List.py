# Merge Sort Solution...分一半，
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # split the list into two halves
        left = head
        right = self.getMid(head)
        # 3/10 接下來三行很重要，要能讓right獨立出來，再進行merge
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        # 不是left=sortList(self,left)
        right = self.sortList(right)
        return self.merge(left, right)
        # 記得self

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            # 不是while head
            slow = slow.next
            fast = fast.next.next
        return slow

    # 不是slow.next

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

        return dummy.next
