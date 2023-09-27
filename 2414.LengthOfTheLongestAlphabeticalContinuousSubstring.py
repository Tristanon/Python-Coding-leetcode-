class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        seenData = set()
        count = 0
        maxCount = 0
        conLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        index = conLetter.index(s[0])
        for i in range(len(s)):
            if index < len(conLetter) and s[i] not in seenData and s[i] == conLetter[index]:
                seenData.add(s[i])
                index += 1
                count +=1
                print(count)
            else:
                seenData = set()
                index = conLetter.index(s[i])
                maxCount = max(count,maxCount)
                count = 0
                if s[i] == conLetter[index]:
                    seenData.add(s[i])
                    count +=1
                    index += 1
        return max(maxCount, count)