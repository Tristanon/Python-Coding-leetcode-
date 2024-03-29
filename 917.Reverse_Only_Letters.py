# First solution
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # creat a list of normal and capital alphabet
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        capital_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # assign "-" in the answer_list
        answer_list = [" "] * len(s)
        for index in range(len(s)):
            if s[index] == "-":
                answer_list[index] = s[index]

        # assgin elements that are not alphabet
        for index in range(len(s)):
            if s[index] not in alphabet and s[index] not in capital_alphabet:
                answer_list[index] = s[index]

        # assign the alphabet with reverse index
        empty_index = 0
        for index in range(len(s)-1,-1,-1):
            while empty_index <= len(answer_list) -1 and answer_list[empty_index] != " ":
                empty_index +=1
            if s[index] in alphabet or s[index] in capital_alphabet:
                answer_list[empty_index] = s[index]

        # return the string with those element in answer_list
        return "".join(answer_list)

#Second solution use two pointer
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        capital_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        left = 0
        right = len(s)-1
        answer = ""
        while left < len(s):
            while right > -1 and s[right] not in alphabet and s[right] not in capital_alphabet:
                right -= 1
            if s[left] not in alphabet and s[left] not in capital_alphabet and left <len(s):
                answer += s[left]
                left +=1
            else:
                answer += s[right]
                left +=1
                right -=1
        return answer 
            