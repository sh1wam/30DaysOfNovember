class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        if not self.hasStar(p):
            return self.isEqual(s, p)
        
        for s_char in set(s):
            if s_char not in p and "." not in p:
                return False
        
        while "**" in p:
            p = p.replace("**", "*")
        
        front_p, remaining_p = self.splitPattern(p)
        if not self.hasStar(front_p):
            front_s, remaining_s = s[:len(front_p)], s[len(front_p):]
            return self.isMatch(remaining_s, remaining_p) and self.isMatch(front_s, front_p)
        else:
            front_p = self.expandStar(s, front_p)
            while len(front_p) >= 0:
                front_s, remaining_s = s[:len(front_p)], s[len(front_p):]
                if self.isMatch(remaining_s, remaining_p) and self.isMatch(front_s, front_p):
                    return True
                if len(front_p) == 0:
                    break
                else:
                    front_p = front_p[:-1]
            return False

    def hasStar(self, p):
        return '*' in p

    def isEqual(self, s, p):
        if len(s) != len(p):
            return False
        
        for s_char, p_char in zip(s, p):
            if s_char != p_char and p_char != ".":
                return False
        
        return True

    def splitPattern(self, p):
        first_star = p.find("*")
        if first_star == 1:
            split_at = first_star + 1
        else:
            split_at = first_star - 1
        front, remaining = p[:split_at], p[split_at:]
        return front, remaining
    
    def expandStar(self, s, p):
        new_p = ""
        if p[0] == ".":
            new_p = "." * len(s)
        else:
            for s_char in s:
                if s_char == p[0]:
                    new_p += s_char
                else:
                    break
        
        return new_p      