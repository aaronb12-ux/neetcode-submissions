import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        
        '''
utilize a stack. the stack will have at most 3 values
it will have 3 if the most recently added item is an operator

iterate through the input. and add to the stack. if we hit a "*, /, +, -"
then do that operation on the two items on the stack. after that operation is done, push that new number to the stack
  
        '''

        stack = []

        evaluation = 0

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            #put the token into the stack if its an integer
            match token:
                case "+":
                    num2 = stack.pop()
                    num1 = stack.pop()

                    evaluation = (num1 + num2)

                    stack.append(evaluation)

                case "*":
                    num2 = stack.pop()
                    num1 = stack.pop()

                    evaluation = (num1 * num2)

                    stack.append(evaluation)


                case "-":
                    num2 = stack.pop()
                    num1 = stack.pop()

                    evaluation = (num1 - num2)

                    stack.append(evaluation)

        
                case "/":
                    num2 = stack.pop()
                    num1 = stack.pop()

                    evaluation = int(float(num1) / float(num2))

                    stack.append(evaluation)

                case _:
                    stack.append(int(token))

        return evaluation

'''
tokens = ["1","2","+","3","*","4","-"]


4
9
stack 

evalulation = 9

num2 = 4
num1 = 9


'''





        