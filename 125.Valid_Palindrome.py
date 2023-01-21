#------------------------------------------------------------------------------------------------------------------------------------#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        dull = s.lower()
        alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','0','1','2','3','4','5','6','7','8','9']
        new_s = ""
        index = 0
        for index in range(len(dull)):
            if dull[index] in alphabet:
                new_s += dull[index]
        self.new_s = new_s
        #check palindrome
        if len(new_s) == 1:
            return True
        if len(new_s) == 0:
            return True
        begin_index = 0
        last_index = len(new_s)-1
        if len(new_s) % 2 == 0:
            val = len(new_s)/2
        else:
            val = (len(new_s)-1)/2
        count = 0
        while True:
            if new_s[begin_index] == new_s[last_index]:
                count +=1
            else:
                return False
            begin_index +=1
            last_index -=1
            if begin_index == last_index or begin_index > last_index:
                break
            # if count == 10:
            #     break
        # self.count = count
        if count == val:
            return True
        else:
            return False

# e = Solution()
# e.isPalindrome("0P")
# print(e.new_s)
#-----------------------------------------------------------------------------------------------------------------------------------#
#Solution 2: Much shorter but worse:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []
        for index in range(len(s)):
            if s[index].isalnum():
                new_list.append(s[index].lower())
            else: 
                pass
        return "".join(new_list) == "".join(new_list[::-1])

# test = Solution()
# test.isPalindrome("A man, a plan, a canal: Panama")
# print(test.list)
            