class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i=0
        T=len(s)-1
        while i<=T:
            s[i],s[T]=s[T],s[i]
            i = i + 1
            T = T - 1
        return s