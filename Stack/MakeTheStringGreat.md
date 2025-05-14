# [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/description)

```py
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1])-ord(c))==32:
                stack.pop()
                continue
            stack.append(c)
        
        return ''.join(stack)
```

```c++
string n;
for (char c : s) {
    if (!n.empty() && abs(n.back() - c) == 32) {
        n.pop_back();
    } else {
        n.push_back(c);
    }
}
return n;
```
