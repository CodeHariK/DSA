# [1992. Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland)

```py
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows , cols = len(land) , len(land[0])
        res = []
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    if (i > 0 and land[i - 1][j] == 1) or (j > 0 and land[i][j - 1] == 1):
                        continue
                    idx = [i , j]
                    row , col = i , j
                    while row < rows and land[row][j] == 1:
                        row += 1
                    while col < cols and land[i][col] == 1:
                        col += 1
                    idx.append(row - 1)
                    idx.append(col - 1)
                    res.append(idx)
        return res
```
