class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



        #if time is LESS than or equal to, it joins the same fleet and does NOT get pushed onto the stack
        #if time is greater than, then its its own fleet and it gets pushed to the stack

        #length of stack at end if the solution


        startingPosandSpeed = []

        for i in range(len(position)):
            startingPosandSpeed.append([position[i], speed[i]])
        
        #now sort startingPosandSpeed based on pos in decreasing order

        sortedArr = sorted(startingPosandSpeed, key=lambda pos: pos[0], reverse=True)

        stack = []

        for car in sortedArr:

            time = (target - car[0]) / car[1]

            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)
        






        