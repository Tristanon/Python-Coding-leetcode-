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