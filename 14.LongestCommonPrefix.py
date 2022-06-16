<<<<<<< HEAD
class Solution:

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]                                                                                                                                                          
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
=======
class Solution:

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]                                                                                                                                                          
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
>>>>>>> 2ea356f2a0fb324ea544d93a3636a794d84960b3
            return reduce(self.lcp,strs)