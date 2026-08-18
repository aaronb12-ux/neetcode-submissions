class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
            monotonic stack:
                    continuously add temperatures to the stack. if the current temperature is g

            the key is to keep the stack in monotonic decreasing order -> its always in decreasing order. So if we come across a temperature that is greater than the top of the stack, continue popping until the current temp is less than the top of the stack


        '''

        res = [0] * len(temperatures)
        stack = [] #stack of pairs: [temp, index in temperatures arr]

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append([t, i])
        
        return res

            




            
            


            

                



        