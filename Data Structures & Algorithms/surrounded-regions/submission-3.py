class Solution:
    def solve(self, board: List[List[str]]) -> None:

        '''
                we can run a multisource bfs from all the 'edge' zeros. all other zero cells part of this bfs, we keep as 0. the others we x out. we keep these coordinates as point in a set.

        '''

        num_rows = len(board)
        num_cols = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        queue = deque([])
        not_surrounded = set()

        def is_edge(row, col):

            if row == 0 or row == num_rows - 1:
                return True
            elif col == 0 or col == num_cols - 1:
                return True
            
            return False

        def in_bounds(i, j):
            return 0 <= i < num_rows and 0 <= j < num_cols
        
        for i in range(num_rows):
            for j in range(num_cols):
                if is_edge(i,j) and board[i][j] == "O":
                    queue.append((i, j))
                    visited.add((i, j))
                    not_surrounded.add((i,j))
        
        
        while queue:

            row, col = queue.popleft()

            for dy, dx in directions:
                next_row = row + dy
                next_col = col + dx

                
                if in_bounds(next_row, next_col):
                    if board[next_row][next_col] == "O" and (next_row, next_col) not in visited:
                        not_surrounded.add((next_row, next_col))
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
        
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == "O" and (i,j) not in not_surrounded:
                    board[i][j] = "X"
        
        return None


        

        