# Note: this problem is essentially writing a matching engine... .

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        ob = [[],[]]                                # init orderbook
        for order in orders:
            o_p, o_amt, o_t = order 
            ob_sub = ob[1 - o_t]                    # push the order into the book of reverse-side 
            while len(ob_sub) > 0 and o_amt > 0:
                b_w, b_p, b_amt = ob_sub[0]    # here, ob_sub is of the contrary type
                if (o_t==0 and o_p >= b_p) or (o_t == 1 and o_p <= b_p):                   
                    matched_amt = min(o_amt, b_amt)
                    o_amt -= matched_amt            # cancelling each other
                    b_amt -= matched_amt            # cancelling each other
                    if b_amt > 0:
                        # Do NOT use heappushpop(ob_sub, (b_w, b_p, b_amt)) coz it causes error!
                        heapreplace(ob_sub, (b_w, b_p, b_amt))
                    else:
                        heappop(ob_sub)
                else:
                    break
            if o_amt > 0:
                new_w = -o_p if o_t == 0 else o_p
                heappush(ob[o_t], (new_w, o_p, o_amt))     
        ans = sum(map(itemgetter(2), ob[0])) + sum(map(itemgetter(2), ob[1]))
        return ans % (10**9+7)
