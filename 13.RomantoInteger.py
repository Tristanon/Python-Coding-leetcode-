class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vd = { 
             "I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000,
             }
        n=len(s)
        rt = 0
        for i in range(n):
            if  i==n-1 or vd[s[i]] >= vd[s[i+1]] :
                rt += vd[s[i]]
            else :
                rt -= vd[s[i]]
                
        return rt