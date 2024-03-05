# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)

```py
class Solution:
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
```
