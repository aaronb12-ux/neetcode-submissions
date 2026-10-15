from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        '''
        use kahns algorithm to find the ordering

        data structures needed:
            need a default dict of a node and its outgoing edges
            number of courses
            in degree list
            queue that stores edges with in_degree == 0
        '''

        
        def make_adj_and_in_degree():

            adj_list = defaultdict(list)
            in_degree = [0] * numCourses

            for pair in prerequisites:
              

                adj_list[pair[1]].append(pair[0])
                in_degree[pair[0]] = in_degree[pair[0]] + 1

            return adj_list, in_degree

        
        adj_list, in_degree = make_adj_and_in_degree()
        queue = deque([])

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        index = 0
        order = [0] * numCourses

        while queue:

            at = queue.popleft()
            order[index] = at

            for to in adj_list[at]:
                in_degree[to] -= 1

                if in_degree[to] == 0:
                    queue.append(to)
            index += 1
        
        if index != numCourses:
            return []
        
        return order






        