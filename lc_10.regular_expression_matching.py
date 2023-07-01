class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pn = len(p)
        sn = len(s)
        prev_layer = {-1}
        pi = 0 
        while pi<pn:
            pchari = p[pi]
            if pi+1<pn and p[pi+1] == '*': # contains *
                if pchari == '.':
                    prev_item = min(prev_layer)
                    curr_layer = set(range(prev_item, sn))
                else:
                    curr_layer = prev_layer.copy()
                    for prev_item in prev_layer:
                        for i in range(prev_item+1, sn):
                            if s[i] == pchari:
                                curr_layer.add(i)
                            else:
                                break
                pi += 2  
            else:
                if pchari == '.':
                    curr_layer = {prev_item+1 for prev_item in prev_layer if prev_item+1 < sn}
                else:
                    curr_layer = {prev_item+1 for prev_item in prev_layer if prev_item+1 < sn and s[prev_item+1]== pchari}
                pi += 1

            if len(curr_layer) == 0:
                return False
            prev_layer = curr_layer
   

            
        return (sn-1) in prev_layer
