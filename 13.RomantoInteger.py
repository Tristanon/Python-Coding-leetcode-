class Solution:
    def romanToInt(self, s: str) -> int:
        SymbolnValue = { 
             "I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000,
        }
        n=len(s)
        result = 0
        for i in range(n):
            if  i==n-1 or SymbolnValue[s[i]] >= SymbolnValue[s[i+1]] :
                result += SymbolnValue[s[i]]
            else :
                result -= SymbolnValue[s[i]]
        return result
        
