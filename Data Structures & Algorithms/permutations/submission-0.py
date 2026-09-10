class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.ans = []

        def back_track(curr):
            
            if len(curr) == len(nums): #base case -> found 
                self.ans.append(curr[:])
                return
            

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    back_track(curr)
                    curr.pop()



        back_track([])
        return self.ans
            


        