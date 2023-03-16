# 451.Sort_Characters_By_Frequency.py
# Solution 1:
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
		# Pass 1, get counts
        d = {}
        for i in s:
            if i not in d:
                d[i] = [i]
            else:
                d[i].append(i)
        #Sort by the length of the letters you've accumulated (ologn i think)
        vals = sorted(d.values(), key= lambda l:len(l), reverse=True)
		#Pass 2, join the sub lists 
        for i in range(len(vals)):
            vals[i]=''.join(vals[i])
		#Pass 3, build your string
        ans=""
        for i in vals:
            ans+=i
        return ans
# Solution 2:
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = []
        for ch in s:
            char.append(ch)
        
        dict = Counter(char)
        lst_sort = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        
        print(lst_sort)
        s = ""
        for tup in lst_sort:
            count = tup[1]
            while count >= 1:
                s += tup[0]
                count -= 1
        return s