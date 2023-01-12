class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kb = dict(knowledge)
        ans = ''
        in_bracket = False
        for i, char_i in enumerate(list(s)):
            match char_i:
                case '(':
                    key_head_idx = i
                    in_bracket = True
                case ')':
                    key = s[key_head_idx + 1:i]     # caveat: the lower bound should be idx+1 (inclusive, and the upper bound should be i (exclusive)!
                    ans += kb.get(key, '?')
                    in_bracket = False
                case _:
                    if not in_bracket:
                        ans += char_i

        return ans
