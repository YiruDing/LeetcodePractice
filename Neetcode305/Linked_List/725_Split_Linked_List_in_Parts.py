
# https://www.youtube.com/watch?v=Fev38Ys6LHw
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        tail = head
        length = 0
        # 2/15 0!!
        while tail:
            length += 1
            tail = tail.next
        width, remainder = length // k, length % k
        cur = head
        prev = None
        
        for i in range(k):
            res.append(cur)
            # 這兩行別忘了！
            for j in range(width):
                if cur:
                    prev = cur
                    cur = cur.next
            if remainder and cur:
                # 這步是上面結束後才做的...縮排要注意！
                    prev = cur
                    cur = cur.next
                    remainder -= 1
            if prev:
                    prev.next = None
        return res
        
        
# 官方解答
class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans