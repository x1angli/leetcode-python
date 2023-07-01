import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        letters = (phoneMap[button] for button in digits)
        ans = [''.join(letter_entry) for letter_entry in itertools.product(*letters)]
        return ans
