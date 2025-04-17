import itertools
class Solution:
    def __init__(self):
        self.comb = []
        self.digit_to_letters = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
            }
    def letterCombinations(self, digits: str):
        return self.combinations(digits)
    
    def combinations(self, digits):
        result = []
        if len(digits) == 1:
            for i in self.digit_to_letters[digits]:
                result.append([i])
        else:
            for i in self.digit_to_letters[digits[0]]:
                x = self.combinations(digits[1:])
                for j in x:
                    result.append([i] + j)
        return result
        

s = Solution()
print(s.letterCombinations("2345"))

        
    