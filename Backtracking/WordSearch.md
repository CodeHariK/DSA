# [79. Word Search]()

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r==m or c<0 or c==n or (r,c) in visited or board[r][c]!=word[i]:
                 return False

            visited.add((r,c))
            if dfs(r+1,c,i+1) or  dfs(r-1,c,i+1) or  dfs(r,c+1,i+1) or dfs(r,c-1,i+1):
                return True
            visited.remove((r,c))

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False
```

