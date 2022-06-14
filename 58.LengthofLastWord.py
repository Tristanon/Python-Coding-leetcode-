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
    