class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
        backtracking:
        at each node all we need is the current sum

        if the current sum is equal to the target, then add that sum to the answer

        

        '''

        ans = []

        def back_track(curr_path, path_sum, index):
           

            if path_sum == target:
                ans.append(curr_path[:])
                return
        
            for j in range(index, len(nums)):

                if path_sum + nums[j] <= target:
                    curr_path.append(nums[j])
                
                    back_track(curr_path, path_sum + nums[j], j) 

                    curr_path.pop()
                
        back_track([], 0, 0)

        return ans
            

        
