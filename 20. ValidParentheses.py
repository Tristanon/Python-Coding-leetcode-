class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=1
        T=0
        L=len(s)
        for i in range(len(s)-1):            
            for j in range(len(s)-1):
                if s[i] == s[j]:
                    T = T + 1
        if T == L/2:
            print("true")
        else:
            print("false")