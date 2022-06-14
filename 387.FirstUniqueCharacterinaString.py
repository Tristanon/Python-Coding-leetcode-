class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        T=0
        j=0
        a=0
        if len(s) > 1:
            for j in range(len(s)):
                if s.count(s[j]) == 1:
                    a = a + 1
            
            if a > 0:
                while T == 0:
                    if s.count(s[i]) == 1:
                        T = T + 1
                    else: 
                        i = i +1
                return s.index(s[i])
            else:
                return -1
        else:
            return 0
        