<<<<<<< HEAD
i=0
T=0
j=0
a=0
s = "leetcode"
if len(s) > 1:
    for j in range(len(s)):
        if s.count(s[j]) == 1:
            a = a + 1
    print(a)        
    if a > 0:
        while T == 0:
            if s.count(s[i]) == 1:
                T = T + 1
            else: 
                i = i +1
        print(s.index(s[i]))
    else:
        print(-1) 
else:
    print(0) 
=======
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split()
        if len(a) == 0:
            return 0
        else:
            return len(a[len(a)-1])
    
>>>>>>> 2ea356f2a0fb324ea544d93a3636a794d84960b3
