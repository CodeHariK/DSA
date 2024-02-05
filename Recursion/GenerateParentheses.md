# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(open, close, curr):
            if(open == n and close == n):
                res.append(curr)
                return
            if(open < n):
                backtracking(open + 1, close, curr + "(")
            if(close < open):
                backtracking(open, close + 1, curr + ")")
        backtracking(0, 0, "")
        return res
```