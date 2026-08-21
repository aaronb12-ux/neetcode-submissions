class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        '''
            run a binary search

            for each middle value, we need to find the row and column of it. Once we do this we can index the 2d array to find the value, if value is equal to the target then return true. otherwise do our normal updating 



        in example: 
        l = 0
        r = 11

        m = 5

        '''





        m = len(matrix) #num rows
        n = len(matrix[0]) #num cols

        left = 0
        right = (m * n) - 1

        while left <= right:

            mid = (left + right) // 2

        
            row = mid // n
            col = mid % n

            val = matrix[row][col]
            print(val)

            if val == target:
                return True
            
            if val < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False




      

        
        