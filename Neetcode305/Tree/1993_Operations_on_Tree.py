class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(parent)
        # if it's locked, the value will be the user
        self.child = {i: [] for i in range(len(parent))}
        # list of their children
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]: return False
        self.locked[num] = user
        # this num is locked by the user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user: return False
        # if you are not the user who locked it, then you cannot unlock it
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i != -1:
            # this loop is to go back to the ancestor until we reach -1.Because parent[0] = -1
            if self.locked[i]:
                return False
            i = self.parent[i]
            # set i == it's parent and keep on going up the chain
        lockedCount = 0
        # To check that it has at least one locked descendant (by any user)
        q = deque([num])
        while q:
            n = q.popleft()
            if self.locked[n]:
                self.locked[n] = None
                # unlock its descentants one by one
                lockedCount += 1
            q.extend(self.child[n])

        if lockedCount > 0:
            # So that we can upgrade the input node
            self.locked[num] = user
        return lockedCount > 0


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)