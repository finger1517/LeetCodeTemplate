class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        res=[]      
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    land=[i,j,-math.inf,-math.inf]
                    self.dfs(grid,i,j,land)
                    res.append(land)
        return res

    def dfs(self,grid,i,j,land):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
            return
        # the most important part!! if you have been to the land, in next travel, you never do it again
        grid[i][j]=0
        land[2]=max(land[2],i)
        land[3]=max(land[3],j)
        # self.dfs(grid,i,j-1,land)
        self.dfs(grid,i,j+1,land)
        # self.dfs(grid,i-1,j,land)
        self.dfs(grid,i+1,j,land)