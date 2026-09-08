from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
            implement a min heap with nums, the heap should always be len k. by the end 
        '''

        heap = []

        for num in nums:

            heappush(heap, num)

            if len(heap) > k:

                heappop(heap)  


        return heap[0]      