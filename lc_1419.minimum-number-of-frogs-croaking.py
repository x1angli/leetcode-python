class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        l_counter = {'c': 0, 'r': 0, 'o': 0, 'a': 0}
        
        def get_prev_l(currl: str) -> str:
            return 'croak'['croak'.index(currl) - 1]
        
        ans = 0
        
        for l in croakOfFrogs:
            if l == 'c':
                l_counter['c'] += 1
                ans = max(ans, sum(l_counter.values()))
            else:
                prev_l = get_prev_l(l)
                if l_counter[prev_l] == 0:
                    return -1
                l_counter[prev_l] -= 1
                if l != 'k':
                    l_counter[l] += 1
        
        if sum(l_counter.values()) > 0:
            return -1
        return ans


class InefficientSolution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        l_2_c = 'croak'
        frogs = []
        ans = 0
        for l in croakOfFrogs:
            match l:
                case 'c': 
                    frogs.append(1)
                    ans = max(ans, len(frogs))
                case 'r':
                    try:
                        frog_i = frogs.index(1)
                        frogs[frog_i] += 1
                    except ValueError:
                        return -1                        
                case 'o':
                    try:
                        frog_i = frogs.index(2)
                        frogs[frog_i] += 1
                    except ValueError:
                        return -1    

                case 'a':
                    try:
                        frog_i = frogs.index(3)
                        frogs[frog_i] += 1
                    except ValueError:
                        return -1                           
                        
                case 'k':
                    try:
                        frog_i = frogs.index(4)
                        del frogs[frog_i]   
                    except ValueError:
                        return -1    
                    
                case _:
                    return -1
        if len(frogs) > 0:
            return -1
        return ans
