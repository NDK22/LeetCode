class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                compare_1 = set(words[i])
                compare_2 = set(words[j])
                if compare_1 ==compare_2:
                    count+=1
        return count
