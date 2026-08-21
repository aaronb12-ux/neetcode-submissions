from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):

        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.timestamps[key].append(timestamp)
        self.values[key].append(value)
    
    def get(self, key: str, timestamp: int) -> str:

        times = self.timestamps.get(key, [])

        #need to somehow check if 'timestamp' exists in this arr

        #[1, 2, 3, 4, 5, 6]

        #we can perform a binary search on the times and see if we can find the target, then return the index
        index = bisect_right(times, timestamp) - 1
      
    
        if index >= 0:

            return self.values[key][index]
        
        return ""






    
        
 
      



        


        
