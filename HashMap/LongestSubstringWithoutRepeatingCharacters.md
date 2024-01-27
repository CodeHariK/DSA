# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

Given a string s, find the length of the longest 

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        c = defaultdict()
        c[s[0]] = 0
        for i in range(1,len(s)):
            if s[i] in c:
                keys = list(c.keys())
                for k in keys:
                    if c[k] < c[s[i]]:
                        c.pop(k)
            c[s[i]] = i
            ans = max(len(c.values()), ans)
        return ans
```