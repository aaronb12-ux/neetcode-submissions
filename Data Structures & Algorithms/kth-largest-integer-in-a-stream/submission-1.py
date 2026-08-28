from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        #add to array then implement a heap on the array by heapifying
        self.stream = [] 
        self.k = k

        '''
            the heap should always be len 'k'. so when we need to pop
            we can just pop the top value 
        '''

        for num in nums:

            heappush(self.stream, num) 

            if len(self.stream) > self.k:

                heappop(self.stream)
        

    def add(self, val: int) -> int:

        heappush(self.stream, val)

        if len(self.stream) > self.k:

            heappop(self.stream)

        return self.stream[0]

        
        
