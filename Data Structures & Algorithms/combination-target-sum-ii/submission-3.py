from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
        no duplicate combinations -> index + 1
        each number can only be used once -> counter

        so only add a number to the current path if it is still available in the candidates

        because we dont want duplicate combinations, keep an index var and increase it by 1 each back_track call
        '''

        ans = []

        candidates.sort()
           
        def back_track(path, path_sum, start):

            if path_sum == target:
                    ans.append(path[:])
                    return
            
            for i in range(start, len(candidates)):

                number = candidates[i]

                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                if number + path_sum <= target:

                    path.append(number)
                    back_track(path, path_sum + number, i + 1)
                    path.pop()
              
        back_track([], 0, 0)

        return ans





        