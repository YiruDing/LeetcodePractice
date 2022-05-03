# DFS
# preMap hashtable{0:[1,2],1:[3,4]....}
class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        # Set the initial value(As a container) for the map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet=all courses along the current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                # it's a loop
                return False
            if preMap[crs] == []:
                return True
            # Above deal with two different situations...
            # Then check the "pre" part in every course we "visited"
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            # Cause we had already finished visiting it

            # 0503
            # Don't forget the following 2 lines!
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

# to be read...
# JS solution
# https://dev.to/cod3pineapple/207-course-schedule-javascript-solution-24e5