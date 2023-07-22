from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = collections.deque([-1])
        ans = 0
        for i, char_i in enumerate(s):
            if char_i == '(':
                stack.append(i)
            else: # char_i == ')'
                stack.pop()
                if stack:
                    lookback_len = i - stack[-1]
                    ans = max(ans, lookback_len)
                else: # stack is empty
                    stack.append(i)
        # end_of_for
        return ans
