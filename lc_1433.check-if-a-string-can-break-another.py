from itertools import accumulate
from collections import Counter

class SolutionCounter:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)
        
        r_26 = range(26)        # shorthand
        a_to_z = [chr(ord('a') + i) for i in r_26]
        
        acc_ch1 = list(accumulate(c1[l] for l in a_to_z))
        acc_ch2 = list(accumulate(c2[l] for l in a_to_z))
            
        return all(acc_ch1[i] >= acc_ch2[i] for i in r_26) or \
               all(acc_ch2[i] >= acc_ch1[i] for i in r_26)
    

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        
        rng = range(len(l1)) # shorthand
            
        return all(l1[i] >= l2[i] for i in rng) or \
               all(l1[i] <= l2[i] for i in rng)    
