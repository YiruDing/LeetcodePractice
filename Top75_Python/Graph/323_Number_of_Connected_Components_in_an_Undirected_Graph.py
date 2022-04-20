class Solution:
    def countComponents(self, n: int, edges: List[List[int]])->int:
        parent = [i for i in range(n)]
        rank = [1]* n
        
        def find(n1):
            # ??? n?
            result = n1
            
            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        # To indicate that we did perform a successful union
                
        result=n
        for n1,n2 in edges:
            result -= union(n1,n2)
        return result
            
            
        