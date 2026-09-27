from collections import deque
import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        '''
            gather all treasures and find closest land cell

        '''

        num_rows = len(grid) 
        num_cols = len(grid[0])
        queue = deque([])
        visited = set()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        def valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        #populate the queue
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))
                    
        while queue:

            row, col, steps = queue.popleft()

            if grid[row][col] != -1 and grid[row][col] != 0: 
                grid[row][col] = steps
                
            
            for dy, dx in directions:
                next_row = row + dy
                next_col = col + dx

                if valid(next_row, next_col):
                    if (next_row, next_col) not in visited:
                        if grid[next_row][next_col] != -1:
                            print("hi")
                            queue.append((next_row, next_col, steps + 1))
                            visited.add((next_row, next_col))
        
        print(grid)
        
        
            
            
        
        
        