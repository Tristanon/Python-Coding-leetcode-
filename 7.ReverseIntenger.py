class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31 - 1) or x < (-2**31):
            return 0
        string = str(x)
        result = '-'
        reverse = string[::-1]
        i = 0
        print(type(reverse))
        if reverse[len(reverse)-1] == '-':
            for i in range(len(reverse)-1):
                result = result + reverse[i]
            return int(result)
        return int(reverse)
