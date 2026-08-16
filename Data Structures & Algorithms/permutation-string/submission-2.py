from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            sliding window problem

            keep track of length of current window. if the length of the current window is greater than or equal to len(s1), and all the chars in s1 havent been seen yet, then reset window

            
        '''

        charsToFind = Counter(s1)
        uniqueChars = set(s1) 
        numsLeftToRemove = len(uniqueChars) #unique chars

        '''
                            
        s1 = "abc", s2 = "lecaabee"

        CharsToFind = l: 1, e: 1, c: 0, a: 2, b: 1, e : 2
        Uniquehars = {a, b, c}
        numLeftToRemove = 3

        currentChar = c

        '''

        left = 0

        for right in range(len(s2)):

            currentChar = s2[right]

            if currentChar in uniqueChars:
                charsToFind[currentChar] -= 1
                if charsToFind[currentChar] == 0:
                    numsLeftToRemove -= 1

            if numsLeftToRemove == 0:
                return True

            if right - left + 1 >= len(s1):
                leftChar = s2[left]
                if leftChar in uniqueChars:
                    if charsToFind[leftChar] == 0:
                        numsLeftToRemove += 1
                    charsToFind[leftChar] += 1
                left += 1
        
        return False
