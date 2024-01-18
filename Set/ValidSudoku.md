# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

## Go

```Go
    func isValidSudoku(board [][]byte) bool {
        seen := make(map[string]bool)

        for i := 0; i < 9; i++ {
            for j := 0; j < 9; j++ {
                number := board[i][j]
                if number != '.' {
                    rowKey := fmt.Sprintf("r", number, i)
                    colKey := fmt.Sprintf("c", number, j)
                    boxKey := fmt.Sprintf("b", number, "_", i/3, "_", j/3)

                    if seen[rowKey] || seen[colKey] || seen[boxKey] {
                        return false
                    }

                    seen[rowKey] = true
                    seen[colKey] = true
                    seen[boxKey] = true
                }
            }
        }

        return true
    }
```

## Java

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set seen = new HashSet();
        for (int i=0; i<9; ++i) {
            for (int j=0; j<9; ++j) {
                char number = board[i][j];
                if (number != '.')
                    if (!seen.add(number + "r" + i) ||
                        !seen.add(number + "c" + j) ||
                        !seen.add(number + "b" + i/3 + "-" + j/3))
                        return false;
            }
        }
        return true;
    }
}
```

## C++

```c++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<string> seen; 
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char number = board[i][j];
                if (number != '.') {
                    if (!seen.insert(to_string(number) + "r" + to_string(i)).second ||
                        !seen.insert(to_string(number) + "c" + to_string(j)).second ||
                        !seen.insert(to_string(number) + "b" + to_string(i/3) + "-" + to_string(j/3)).second)
                        return false;
                }
            }
        }
        return true;
    }
};
```

## Py

```py
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [
                        f'r_{i}_{element}', 
                        f'c_{j}_{element}', 
                        f'b_{i // 3}_{j // 3}_{element}', 
                    ]
        return len(res) == len(set(res))
```
