class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.split()
        len_last = len(list_s[-1])
        return len_last
