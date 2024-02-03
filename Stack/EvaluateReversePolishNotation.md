# (150. Evaluate Reverse Polish Notation)[https://leetcode.com/problems/evaluate-reverse-polish-notation/description/]

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


```py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        op  = ["*","/","+","-"]
        for c in tokens:
            if c in op:
                y = ans.pop()
                x = ans.pop()
                a = 0
                if c == "*": a = x * y
                if c == "/": a = math.trunc(x / y)
                if c == "+": a = x + y
                if c == "-": a = x - y
                ans.append(a)
            else:
                ans.append(int(c))

        return ans[0]
```