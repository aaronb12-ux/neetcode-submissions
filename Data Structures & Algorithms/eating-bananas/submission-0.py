import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ''' 
                binary search on a solution space


                our solution space is the numbers of bananas we 
                eat per hour 

                the minimum is 1, and the max is the greatest values in the input array


        min is 1 because for example: if we have [100,500] and h = 600, then we have 600 hours to eat all the bananas. and the min we can do this for is 1 -> one banana per hour

        max is the max of the input because there would be no reason to eat more than the max, because we can only eat a set amount per hour
        '''

        left = 1
        right = max(piles)
        minK = 0

        def hoursTaken(k):

            '''
                trying to eat k bananas per hour
            '''
            hours = 0

            for pile in piles:
                hours = hours + math.ceil(pile / k)
    
            return hours

        while left <= right:
            print(left, right)

            mid = (left + right) // 2

            hours = hoursTaken(mid)
        
            if hours <= h:

                minK = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return minK
            

        