# [2370. Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence)

```py
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        length = len(s)

        # Initialize all dp values to -1 to indicate non-visited states
        dp = [[-1] * 26 for _ in range(length)]

        def dfs(index: int, char: int, dp: list, string: str, k: int) -> int:
            # Memoized value
            if dp[index][char] != -1:
                return dp[index][char]

            # State is not visited yet
            dp[index][char] = 0
            match = char == (ord(string[index]) - ord('a'))
            if match:
                dp[index][char] = 1

            # Non-base case handling
            if index > 0:
                dp[index][char] = dfs(index - 1, char, dp, string, k)
                if match:
                    for prev_char in range(26):
                        if abs(char - prev_char) <= k:
                            dp[index][char] = max(dp[index][char], dfs(index - 1, prev_char, dp, string, k) + 1)
            return dp[index][char]

        # Find the maximum dp[N-1][char] and return the result
        max_length = 0
        for char in range(26):
            max_length = max(max_length, dfs(length - 1, char, dp, s, k))
        return max_length
```
