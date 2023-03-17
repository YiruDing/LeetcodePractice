class Solution:

    def numTrees(self, n: int) -> int:
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] +
        #              numTree[3] * numTree[0]
        numTree = [1] * (n + 1)
        # because we are going from 0 to n

        # 0 node = 1 tree
        # 1 node = 1 tree
        # 從 2 nodes開始跑
        for nodes in range(2, n + 1):
            # 3/16 nodes 的數量可以從2-n
            total = 0
            for root in range(1, nodes + 1):
                # 3/16 大家輪流當root...記得上限是node + 1(不包括本身)
                left = root - 1
                right = nodes - root
                # 3/16左右的node數，分別如上
                total += numTree[left] * numTree[right]
                # 3/16 左右的各種排列組合
                # 12/9 不是 left * right
            numTree[nodes] = total
        return numTree[n]
