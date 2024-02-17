class Solution:
    def romanToInt(self, s: str) -> int:
        # output=0
        # roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # j=0
        # while j< len(s)-1:
        #     if s[j] == 'I' and s[j+1] in ['V','X']:
        #         output += roman_dict[s[j+1]] -1
        #         print(output)
        #         j+=2
        #     elif s[j] == 'X' and s[j+1] in ['L','C']:
        #         output += roman_dict[s[j+1]] -10
        #         print(output)
        #         j+=2
        #     elif s[j] == 'C' and s[j+1] in ['D','M']:
        #         output += roman_dict[s[j+1]]-100
        #         print(output)
        #         j+=2
        #     else:
        #         output += roman_dict[s[j]]
        #         j+=1
        # if j ==len(s)-1:
        #     output += roman_dict[s[j]]
        # return output

        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in s:
            value = roman_values[char]
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        
        return total
