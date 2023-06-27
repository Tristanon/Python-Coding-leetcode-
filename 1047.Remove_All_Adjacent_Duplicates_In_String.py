# Solution 1: using stack to solve the problem but make problems with if statements 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []
        for char in s:
            # need to be imroved
            if not char_stack:
                char_stack.append(char)
            elif char != char_stack[-1]:
                char_stack.append(char)
            else:
                char_stack.pop()
        return "".join(char_stack)
        