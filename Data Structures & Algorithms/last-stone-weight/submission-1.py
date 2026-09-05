from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            keep a max heap.
            each iteration pop the two largest elements from the heap
        '''

        heap = []

        for stone in stones:

            heappush(heap, -stone) 
        
        print(heap)

        while len(heap) >= 2:

                x = abs(heappop(heap))
                y = abs(heappop(heap))
                print(abs(x), abs(y))

                if x != y:
                    new = abs(y - x)

                    heappush(heap, -new)
                
        
        if heap:
            return abs(heap[0]) 
        else:
            return 0


        