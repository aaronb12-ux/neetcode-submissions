class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        ans = []

        number_to_digit = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def back_track(curr_combo, index):

            if len(curr_combo) == len(digits):
                ans.append("".join(curr_combo[:]))
                return
            
            chars = number_to_digit[digits[index]]

            for char in chars:
                curr_combo.append(char)
                back_track(curr_combo, index + 1)
                curr_combo.pop()
        
        back_track([], 0)

        return ans

        