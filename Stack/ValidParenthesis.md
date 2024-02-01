# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

```py
class Solution(object):
    def isValid(self, s):
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0
```