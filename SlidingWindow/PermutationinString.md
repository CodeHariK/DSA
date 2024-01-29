# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = Counter(s1)
        h2 = Counter(s2[0: len(s1)])
        for i in range(len(s2) - len(s1)+1):
            if i > 0:
                h2[s2[i - 1]] -= 1
                if i + len(s1) <= len(s2):
                    h2[s2[i + len(s1) - 1]] += 1
            if h1 == h2:
                return True
        return False

```
