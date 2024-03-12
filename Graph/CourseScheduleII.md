# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

```py
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res,visited = [],{}
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node]=True

            for nei in graph[node]:
                if dfs(nei):
                    return True

            visited[node]=False
            res.append(node)

        for i in range(numCourses):
            if dfs(i):
                return []
        
        return res
```
