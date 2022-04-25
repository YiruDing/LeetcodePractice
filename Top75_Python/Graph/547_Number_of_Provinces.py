# a.k.a Friend Circles
# https://www.youtube.com/watch?v=HHiHno66j40

# Looks like the island question...
# https://www.youtube.com/watch?v=YbCpAU5g0rg


# Also see 200
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        stack = []
        # 200use the queue

        for i in range(len(isConnected)):
            if i not in visited:
                stack.append(isConnected[i])
                while stack:
                    city = stack.pop()
                    for j in range(len(city)):
                        if city[j] == 1 and j not in visited:
                            stack.append(isConnected[j])
                            visited.add(j)
                provinces += 1
        return provinces