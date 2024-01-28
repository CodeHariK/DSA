# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

```py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output,left,dic=0,0,{}
        for right in range(len(s)):
            dic[s[right]]=1+dic.get(s[right],0)
            while (right-left+1)-max(dic.values())>k:
                dic[s[left]]-=1
                left+=1
            output=max(output,right-left+1)
        return output
```
