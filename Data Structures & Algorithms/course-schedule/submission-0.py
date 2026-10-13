from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def make_adj_list(graph): #make adj list

            adj_list = defaultdict(list)

            for pair in graph:
                adj_list[pair[1]].append(pair[0])
            
            return adj_list
        
        #declare vars
        adj_list = make_adj_list(prerequisites)
        n = numCourses
        in_degree = [0] * n

        for pair in prerequisites:
            in_degree[pair[0]] = in_degree[pair[0]] + 1
        
        queue = deque([])

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        index = 0
        order = [0] * n

        while queue:

            at = queue.popleft()
            order[index] = at

            for to in adj_list[at]:
                in_degree[to] = in_degree[to] - 1
                if in_degree[to] == 0:
                    queue.append(to)
            index += 1
            
            
        if index != n:
            return False
            
        return True
        
        
        














        