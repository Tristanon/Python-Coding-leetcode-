<<<<<<< HEAD
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
=======
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
>>>>>>> 2ea356f2a0fb324ea544d93a3636a794d84960b3
            print("false")