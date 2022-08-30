--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Solution 1:
class Solution:
    def isValid(self, s: str) -> bool:
        listopen = []
        openmark = ('([{')
        closemark = (')]}')
        check = {')':'(','}':'{',']':'['}
        for i in s:
            if i in openmark:
                listopen.append(i)
            if i in closemark:
                if not listopen:
                    return False
                elif listopen.pop() != check[i]:
                    return False
                else:
                    continue
        if not listopen:
            return True
        else:
            return False
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
