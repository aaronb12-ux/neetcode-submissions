class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        '''
            need to use backtracking because we are asked to find 'all' combinations

        need to find all possible combinations of k numbers in range [1, n]

this is basically subsets of length k?
        '''
        ans = []

        def back_track(curr, i):

            if len(curr) == k:
                ans.append(curr[:])
                return 
            
            for j in range(i, n + 1):
                curr.append(j)
                back_track(curr, j + 1)
                curr.pop()
        

        back_track([], 1)

        return ans






        