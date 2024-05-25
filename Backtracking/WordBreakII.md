# [140. Word Break II](https://leetcode.com/problems/word-break-ii)

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        def backtrack(i, arr):
            if i == len(s):
                res.append(arr[:])
                return
            elif i > len(s):
                return
            
            for word in wordDict:
                if s[i:].startswith(word):
                    arr.append(word)
                    backtrack(i + len(word), arr)
                    arr.pop()
            
        backtrack(0, [])

        sentences = []
        for arr in res:
            sentences.append(' '.join(arr))
        return sentences
```
