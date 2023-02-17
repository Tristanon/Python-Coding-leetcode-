# First solution: using slice
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        letter_list = []
        
        if ch not in word:
            return word

        for index in range(len(word)):
            letter_list.append(word[index])
            if word[index] == ch:
                letter_list = letter_list[::-1]
                return ''.join(letter_list) + word[index + 1: len(word)]

# Second solution
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        prefix_reverse = []
        prefix_sum = ""
        for index in range(len(word)):
            prefix_sum = word[index] + prefix_sum
            prefix_reverse.append(prefix_sum)

        for i in range(len(prefix_reverse)):
            if prefix_reverse[i][0] == ch:
                return prefix_reverse[i] + word[i + 1: len(word)] 