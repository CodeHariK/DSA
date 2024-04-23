# [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees)

```py
class Solution:
    # trim leaves
    # based on the intuition that a leaf cannot be the root of a MHT as they don't have the min height
    # because all we need to do is take its neighbor as the root instead and we'll get its height - 1

    # another intuition is that this basically does the same thing as the find diameter solution, except it starts trimming right away without finding the diameter first
    # this works because as we trim the leaves from outside in, the trimming process of paths other than the diameter will "wait" for it when it reaches a node that the diameter hasn't reached yet
    # => essentially we're just trimming the diameter until we reach the center(s) anyway

    # Time: O(V + E) - go through all edges O(E) then go through all leaves O(V)
    # Space: O(V + E) - store all edges O(E) then store all leaves O(V)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # build adj list
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        leaves = [k for k in adj_list.keys() if len(adj_list[k]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = list()

            for leaf in leaves:
                neighbor = adj_list[leaf].pop()  # a leaf => has only 1 neighbor
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

    # # 2 pass solution using diameter finding algo
    # # Time: O(V + E)
    # # Space: O(V + E)
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     adj_list = defaultdict(set)
    #     for a, b in edges:
    #         adj_list[a].add(b)
    #         adj_list[b].add(a)

    #     def dfs_longest_path(curr: int, visited: Set[int]) -> List[int]:
    #         visited.add(curr)
    #         unvisited_neighbors = adj_list[curr] - visited

    #         # base case (reaching a leaf)
    #         if not unvisited_neighbors:
    #             return [curr]

    #         max_subpath = list()
    #         for neighbor in unvisited_neighbors:
    #             local_max_path = dfs_longest_path(neighbor, visited)
    #             if len(local_max_path) > len(max_subpath):
    #                 max_subpath = local_max_path

    #         max_subpath.append(curr)
    #         return max_subpath

    #     longest_path_from_0 = dfs_longest_path(0, set())

    #     # longest_path_from_0[0] is the furthest leaf we can reach from 0 (a randomly chosen node)
    #     # => an end point of the diameter
    #     diameter_path = dfs_longest_path(longest_path_from_0[0], set())
    #     mid = len(diameter_path) // 2

    #     if len(diameter_path) % 2 == 1:
    #         return [diameter_path[mid]]
    #     else:
    #         return [diameter_path[mid], diameter_path[mid - 1]]

    # # brute force dfs - TLE
    # # from each node, find the height if that node was the root
    # # Time: O(V * (V + E)) - for each node potentially traverse the whole graph to find its height
    # # Space: O(V + E) - store all edges + recursive space
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     if n == 1:
    #         return [0]

    #     # build adj list
    #     adj_list = defaultdict(list)
    #     for a, b in edges:
    #         adj_list[a].append(b)
    #         adj_list[b].append(a)

    #     def dfs_find_height(curr: int, height: int, seen: Set[int]) -> int:
    #         # shortcircuiting because this can't be the min height
    #         if height > min_height:
    #             return height

    #         adj_nodes = adj_list[curr]
    #         max_height = float("-inf")

    #         for adj_node in adj_nodes:
    #             if adj_node not in seen:
    #                 seen.add(adj_node)
    #                 adj_height = dfs_find_height(adj_node, height + 1, seen)
    #                 seen.remove(adj_node)

    #                 max_height = max(max_height, adj_height)
    #                 if max_height > min_height:
    #                     return max_height

    #         return max(height, max_height)

    #     # dfs_find_height each node in adj list
    #     min_height = float("inf")
    #     min_roots = list()
    #     for node in adj_list:
    #         height = dfs_find_height(node, 0, {node})
    #         if height == min_height:
    #             min_roots.append(node)
    #         if height < min_height:
    #             min_height = height
    #             min_roots = [node]

    #     return min_roots
```
