# [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch)

```py
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mycounter = Counter(students)

        for sandwitch in sandwiches:
            if mycounter[sandwitch] == 0:
                break
            else:
                mycounter[sandwitch] -= 1
        
        return mycounter.total()
```
