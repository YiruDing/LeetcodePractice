# We will use two passes
# 1. clone(create a hashmap to map the old to the new) and add to the linked list
# 2. Connecting/set the pointer


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        # hashMap

        cur = head
        while cur:
            # Copy the node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            # hashMap
            # mapping the old node to the copy node
            cur = cur.next

        cur = head
        while cur:
            # Set the pointer
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
        # 9:09