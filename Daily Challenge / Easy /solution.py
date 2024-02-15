class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        stop_flag = False
        output =''
        for word in words:
            if word == word [::-1]:
                output = word
                stop_flag= True
            if stop_flag:
                break
        return output
