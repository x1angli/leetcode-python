class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 0:
            return ""

        max_p_len = 1
        ans = s[0]

        def expand():
            nonlocal l, r, p_len, max_p_len, ans
            while l >=0 and r<n and s[l]==s[r]:
                if p_len > max_p_len:
                    max_p_len = p_len
                    ans = s[l:r+1]
                l -= 1
                r += 1
                p_len += 2

        for i in range(1, n-1):
            l = i-1
            r = i+1
            p_len = 3
            expand()

        for i in range(n-1):
            l = i
            r = i+1
            p_len = 2
            expand()

        return ans
