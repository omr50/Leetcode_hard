from collections import defaultdict 

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not len(edges):
            return 1
        graph = defaultdict(list)

        for fr, to in edges:
            graph[fr].append(to)
        # test dfs
        node_colors = defaultdict(lambda: [0]*26)
        visited = set()
        perma_visited = set()

        def dfs(graph, curr_node):
            if curr_node in perma_visited:
                return
            if curr_node in visited:
                # print("Cycle")
                return -1
            else:
                visited.add(curr_node)

            # have a size 26 list of 0's and then
            # fill with the maximum colors from each basically
            # this should yield the correct colors
            # because we are guaranteed to update the
            # colors down in the dfs before the current ones
            # and therefore 
            for node in graph[curr_node]:
                if dfs(graph, node) == -1:
                    return -1
                for i in range(0, 26):
                    node_colors[curr_node][i] = max(node_colors[curr_node][i], node_colors[node][i])
            if curr_node not in perma_visited: 
                node_colors[curr_node][ord(colors[curr_node]) - ord('a')] += 1
                perma_visited.add(curr_node)


            visited.remove(curr_node) 
                
        for edge in edges:
        
            if dfs(graph, edge[0]) == -1:
                return -1
        maximum = 0
        for node in node_colors.values():
            maximum = max(maximum, max(node))
        return maximum 
# is there a chance of a feed back loop or accidentally counting a node more than once?

