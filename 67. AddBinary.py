class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = min(len(a),len(b))
        res = ''
        carry = 0
        for i in range(1,length+1):
            if int(a[-i]) + int(b[-i]) + carry > 1:
                res = str(int(a[-i]) + int(b[-i]) + carry - 2) + res
                carry = 1
            else:
                res = str(int(a[-i]) + int(b[-i]) + carry) + res
                carry = 0
        if len(a) > len(b):
            rest = a[:(len(a)-length)]
        elif len(a) < len(b):
            rest = b[:(len(b)-length)]
        else:
            rest = ""
        for i in range(1,len(rest)+1):
            if int(rest[-i]) + carry > 1:
                res = str(int(rest[-i]) + carry - 2) + res
                carry = 1
            else:
                res = str(int(rest[-i]) + carry ) + res
                carry = 0
        if carry == 0:
            return res
        else:
            return "1"+res
