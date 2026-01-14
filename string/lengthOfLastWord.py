class Solution(object):
    def lengthOfLastWord(self, s):


        
        s_temp = ''
        for i in s:
            if i == " ":
                s_temp = ''
            else:
                s_temp += i
                

        print(len(s_temp))


Solution().lengthOfLastWord("hello sam its callum")
