from collections import defaultdict
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''
            run a bfs from all starting locations of the atlantic and pacific

            essentially the edges along the pacific and atlantic

            positions are valid if the next neighbor is greater than or equal to.

            do this for both sides, and common coordinates are the solution

            harder part is figuring out the starting positions.

            starting positions for Pacific:

                num_rows = len(heights)
                num_cols = len(heights[0])

                Pacific Starting Points:
                    row where i = 0
                    cols where j = 0

                Atlantic Starting Points:
                    row where i = (final)
                    col where j = (final)            
        '''


        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific_queue = deque([])
        atlantic_queue = deque([])

        pacific_visited = set()
        atlantic_visited = set()

        pacific_ans = set()
        atlantic_ans = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #fill the queues

        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    pacific_queue.append((i,j))
                    pacific_ans.add((i,j))
                if i == num_rows - 1 or j == num_cols - 1:
                    atlantic_queue.append((i,j))
                    atlantic_ans.add((i,j))

        
        def valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

    
        def bfs(queue, visited, ans):

            while queue:

                row, col = queue.popleft()

                for dy, dx in directions:
                    next_row = row + dy
                    next_col = col + dx

                    if valid(next_row, next_col):
                        if (next_row, next_col) not in visited:
                            if heights[next_row][next_col] >= heights[row][col]:
                                ans.add((next_row, next_col))
                                queue.append((next_row, next_col))
                                visited.add((next_row, next_col))


                      
            
            return ans
    
        pacific_ans = bfs(pacific_queue, pacific_visited, pacific_ans)
        atlantic_ans = bfs(atlantic_queue, atlantic_visited, atlantic_ans)

        ans = []

        for coord in pacific_ans:
            if coord in atlantic_ans:
                ans.append(coord)

        
        return ans
    
        
        
        
        
                            




        
        




        







        