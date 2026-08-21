from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #do 3 specific checks? check rows, columns and the sub boxes

        '''
        first check all rows: make sure there are no duplicates
                loop through and keep a set. add ints to the set. if the int exists in the set return false



        second check all cols: make sure there are no duplocates
            same logic for rows
        '''

          
        def areRowsValid():
            numSet = set()
            for i in range(9):
                
                for j in range(9):

                    if board[i][j].isdigit():

                        if int(board[i][j]) in numSet:
                            return False
                        else:
                            numSet.add(int(board[i][j]))
                
                numSet.clear()

            return True
           
        def areColsValid():
            numSet = set()
            currentRow = 0

            while currentRow < 9:

                for i in range(9):

                    if board[i][currentRow].isdigit():

                        if int(board[i][currentRow]) in numSet:
                            return False
                        else:
                            numSet.add(int(board[i][currentRow]))
                numSet.clear()
                currentRow += 1

            return True

        def areSubBoxesValid():

            subBox = 1

            while subBox < 10: #checking 9 subboxes

                match subBox:

                    case 1:
                        rowStart = 0
                        rowEnd = 2
                        colStart = 0
                        colEnd = 2

                    case 2:
                        rowStart = 0
                        rowEnd = 2
                        colStart = 3
                        colEnd = 5
                    
                    case 3:
                        rowStart = 0
                        rowEnd = 2
                        colStart = 6
                        colEnd = 8
                    
                    case 4:
                        rowStart = 3
                        rowEnd = 5
                        colStart = 0
                        colEnd = 2
                    
                    case 5:
                        rowStart = 3
                        rowEnd = 5
                        colStart = 3
                        colEnd = 5
                    
                    case 6:
                        rowStart = 3
                        rowEnd = 5
                        colStart = 6
                        colEnd = 8
                    
                    case 7:
                        rowStart = 6
                        rowEnd = 8
                        colStart = 0
                        colEnd = 2
                    
                    case 8:
                        rowStart = 6
                        rowEnd = 8
                        colStart = 3
                        colEnd = 5
                    
                    case 9:
                        rowStart = 6
                        rowEnd = 8
                        colStart = 6
                        colEnd = 8
            
                numSet = set()
                for i in range(rowStart, rowEnd + 1):

                    for j in range(colStart, colEnd + 1):

                        if board[i][j].isdigit():

                            if int(board[i][j]) in numSet:
                                return False
                            else:
                                numSet.add(int(board[i][j]))
                
                subBox += 1

            return True
        
        return areSubBoxesValid() and areColsValid() and areRowsValid()
            




            
        
      



        


        
        