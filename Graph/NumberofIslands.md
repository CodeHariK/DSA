# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    count  += 1
        #print(grid)
        return count
    # use a helper function to flip connected '1's to 0
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dr
            c = j + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)
```
