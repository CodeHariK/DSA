# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/description/)

```py
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"): return "0"
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                res[i + j + 1] += (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'));
                res[i + j] += res[i + j + 1] // 10;
                res[i + j + 1] %= 10;

        while i in res:
            if res[0] == 0: res.pop(0)
            else: break

        return ("".join((str(x) for x in res)))
```
