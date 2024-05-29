# [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget)

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = l = currCost = 0
        
        for r in range(len(s)):
            currCost+= abs(ord(s[r]) - ord(t[r]))
            while currCost>maxCost:
                currCost-= abs(ord(s[l]) - ord(t[l]))
                l+=1
            ans = max(ans,r-l+1)
        
        return ans
