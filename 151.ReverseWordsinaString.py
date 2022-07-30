class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()[::-1]
        i = 0
        result = ''
        for i in range(len(a)):
            if i == 0:
                result = a[i]
            else:
                result = result + ' ' + a[i]
        return result
