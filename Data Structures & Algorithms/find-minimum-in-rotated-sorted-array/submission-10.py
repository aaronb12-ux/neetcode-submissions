class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1


        while left < right:
            
            middle = (left + right) // 2
         
            if nums[middle] >= nums[right]:
                left = middle + 1
            else:
                right = middle
            
        return nums[left]

        '''

            [3,4,5,6,1,2]
            l = 0
            r = 5
            m = 2
                   l r
            [3,4,5,6,1,2]

            4 5


            



        '''
            
            
            
            



   




        