class Solution:
    def isMatch(self, s, p):
        s_idx = 0
        p_idx = 0
        match = 0
        star = -1

        while s_idx < len(s):
            if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                match = s_idx
                star = p_idx
                p_idx += 1
            elif star != -1:
                p_idx = star + 1
                match += 1
                s_idx = match
            else:
                return False

        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1

        return p_idx == len(p)
