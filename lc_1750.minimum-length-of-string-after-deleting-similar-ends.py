## Note: the crux of this problem is to understand the question.
###  if what's left is a string with same letters, the problem boils down to the question: is the length of the string is 1 or longer than 1?

class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0 
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return r + 1 - l 
            else:
                same_char = s[l]
                while l < len(s) and s[l] == same_char:
                    l += 1
                while r >= 0 and s[r] == same_char:
                    r -= 1
                   
        return 1 if (l - r) == 2 else 0  
      
