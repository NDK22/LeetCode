class Solution:
    def reverseWords(self, s: str) -> str:
        each_word = s.split()
        reversed_words= reversed(each_word)
        reversed_string = ' '.join(reversed_words)
        return reversed_string
