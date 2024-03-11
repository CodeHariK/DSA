# [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

```py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preq = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preq[c].append(p)

        taken = set()

        def dfs(crs):
            if crs in taken:
                return False
            if preq[crs] == []:
                return True

            taken.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False

            taken.remove(crs)
            preq[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
```
