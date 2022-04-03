class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        # Set the initial value(As a container) for the map
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet=all courses along the current DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                # it's a loop
                return False
            if preMap[crs] ==[]:
                return True
            # Above deal with two different situations...
            # Then check the "pre" part 
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True    
        