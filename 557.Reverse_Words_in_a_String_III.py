# First solution
class Solution:
    def reverseWords(self, s: str) -> str:
        list_letter = s.split(" ")
        answer = list_letter[0][::-1]
        for index in range(1,len(list_letter)):
            answer += " " + list_letter[index][::-1]
        return answer