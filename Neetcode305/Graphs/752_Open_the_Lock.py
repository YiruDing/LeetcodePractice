from collections import deque


# BFS
class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                # 因為是四位數啊！
                digit = str((int(lock[i]) + 1) % 10)
                # 往前轉一格，除以十，使之在 0 ~ 9 之間
                res.append(lock[:i] + digit + lock[i + 1:])
                # 修改一位數，讓他回到str狀態
                digit = str((int(lock[i]) - 1 + 10) % 10)
                # 往後轉一格，但是需要加十，0 - 1 才不至於有負數
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        # indetation!!

        q = deque()
        # deque()!
        q.append(['0000', 0])  #[lock,turns]
        # This is the starting point
        visit = set(deadends)
        # 要避免遇到deadends

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
                    # parent 是 turns, child 要加一
        return -1
        # 如果已經遍歷而不可得，return -1