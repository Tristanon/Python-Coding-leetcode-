# First Solution: 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def popchar(s):
            char_stack = []
            for char in s:
                if char != "#":
                    char_stack.append(char)
                else:
                    if char_stack:
                        char_stack.pop()
            return "".join(char_stack)
        
        s = popchar(s)
        t = popchar(t)
        if s == t:
            return True
        return False
