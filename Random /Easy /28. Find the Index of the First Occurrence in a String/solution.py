class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenght_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+lenght_needle] == needle:
                return i
        return -1
