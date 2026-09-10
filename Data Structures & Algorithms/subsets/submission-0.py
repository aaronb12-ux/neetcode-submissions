class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.ans = []
        n = len(nums)
    
        def back_track(curr, i):
            
            if i > len(nums):
                return
            
            self.ans.append(curr[:])
                
            
            for j in range(i, n):
                    curr.append(nums[j])
                    back_track(curr, j + 1)
                    curr.pop()
            
        back_track([], 0)
        return self.ans






        