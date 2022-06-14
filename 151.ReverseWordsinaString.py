class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()[::-1]
        i = 0
        ketqua = ''
        for i in range(len(a)):
            if i == 0:
                ketqua = a[i]
            else:
                ketqua = ketqua + ' ' + a[i]
        return ketqua