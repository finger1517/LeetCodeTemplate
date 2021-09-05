class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def find_block(i,j):
            p,q = i,j
            while p < m:
                if land[p+1][j]==1:
                    p+=1
            while q < n:
                if land[p][q]==1:
                    q+=1
            return i,j,p,q
                
                
        def search(i,j):
            
        m = len(land)
        n = len(land[0])
        i,j = 0,0
        while i<m:
            while j<n:
                if land[i][j]==1:
                    block = find_block(i,j)
                    x1,y1,x2,y2 = block
            
                    
            
        