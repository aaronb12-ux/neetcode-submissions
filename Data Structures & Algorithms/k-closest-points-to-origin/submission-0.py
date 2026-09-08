from heapq import *
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)

            heappush(heap, [-distance, [x,y]]) 

            if len(heap) > k:
                heappop(heap)
        
        
        ans = []

        for point in heap:
            ans.append(point[1])
        
        
        return ans
        
        
        


        