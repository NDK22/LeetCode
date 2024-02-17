class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        stop_flag=False
        output= ''
        for i in range(len(strs[0])):
            character = strs[0][i]
            for string in strs:
                if string[i] != character:
                    stop_flag=True
            if stop_flag is True:
                break
            output += character       
        return output

                
