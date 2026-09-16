import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
            binary search on a solution space

            1. figure out solution space
            2. perform binary search
            3. for each middle check if its valid
            4. depending on the problem either check bigger or smaller values of the middle


            left = 1
            right = max(piles)
        '''

        left = 1
        right = max(piles)
        best = float("inf")


        def is_valid(k):

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / k)

            
            return hours_taken <= h


        while left <= right:

            middle = (left + right) // 2

            if is_valid(middle):
                best = middle
                right = middle - 1
            
            else:
                left = middle + 1

        return best
            
            





        