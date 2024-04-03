# time and space complexity is O(N)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r , c)
                    count+=1
        return count
    
    
    
    def dfs(self, grid, r , c):
        if r<0 or c<0 or r >=len(grid) or c >= len(grid[0]) or grid[r][c]!= "1":
            return
        
        grid[r][c] = "#"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
        
        