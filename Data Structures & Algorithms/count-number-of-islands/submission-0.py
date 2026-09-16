class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        '''
                this is a grid problem
                iterate through the grid and whenever we come across a 1, incrament the number of islands and perform a DFS.
        '''

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        num_of_islands = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()


        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):

            for dy, dx in directions:
                next_row = row + dy
                next_col = col + dx

               
                if valid(next_row, next_col):
                    if grid[next_row][next_col] == "1":
                        if (next_row, next_col) not in visited:
                            visited.add((next_row, next_col))
                            dfs(next_row, next_col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        visited.add((i, j))
                        num_of_islands += 1
                        dfs(i, j)

        return num_of_islands

        


        







        