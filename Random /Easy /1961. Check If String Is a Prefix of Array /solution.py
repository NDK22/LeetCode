class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        check =''
        for word in words:
            check += word
            if check == s:
                return True
