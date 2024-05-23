# [2597. The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/)

```py
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i, count):
            if i == len(nums):
                return 1

            result = dfs(i + 1, count)

            if not count[nums[i] - k] and not count[nums[i] + k]: 
                count[nums[i]] += 1
                result += dfs(i + 1, count)
                count[nums[i]] -= 1
            return result

        return dfs(0, defaultdict(int)) - 1
```
