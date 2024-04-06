# [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/)

```py
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            elif item == ')':
                if stack:
                    stack.pop()
                else:
                    s[index] = ''
        for item in stack:
            s[item] = ''

        return "".join(s)
```
