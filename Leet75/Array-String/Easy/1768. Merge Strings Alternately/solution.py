class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        concatinated_word= ''
        minimum_length = min(len(word1),len(word2))
        for letter1, letter2 in zip(word1,word2):
            concatinated_word += letter1 + letter2
        if len(word1) > len(word2):
            concatinated_word = concatinated_word + word1[minimum_length:]
        if len(word2) > len(word1):
            concatinated_word = concatinated_word + word2[minimum_length:]
        return concatinated_word
