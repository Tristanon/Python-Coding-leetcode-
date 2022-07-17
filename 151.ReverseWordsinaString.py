class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()[::-1]
        i = 0
        result = ''
        for i in range(len(a)):
            if i == 0:
                result = a[i]
            else:
                result = result + ' ' + a[i]
        return result
