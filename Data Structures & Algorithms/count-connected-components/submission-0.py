from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        '''
            loop from 0 - n - 1 and perform a dfs for each unvisited node. each dfs we perform incrament our answer by 1
        '''

        def make_adj_list():

            adj_list = defaultdict(list)

            for n1, n2 in edges:

                adj_list[n1].append(n2)
                adj_list[n2].append(n1)
            
            return adj_list
        


        adj_list = make_adj_list()
        visited = set()
        ans = 0

        def dfs(node):

            for neighbor in adj_list[node]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):

            if i not in visited:
                visited.add(i)
                dfs(i)
                ans += 1
        
        return ans




        