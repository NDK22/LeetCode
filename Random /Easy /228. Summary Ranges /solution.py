class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        set_nums = nums
        result =[]
        for number in set_nums:
            if number -1 not in set_nums:
                gap = 1
                left = number
                while left + gap in set_nums:
                    gap +=1
                if gap > 1:
                    result.append(str(left)+"->"+str(left+gap-1))
                else:
                    result.append(str(number))
        return result


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]
        for number in nums:
            if ranges and ranges[-1][1]==number -1:
                ranges[-1][1]=number
            else:
                ranges.append([number,number])
        return [ f'{x}->{y}' if x!=y else f'{x}' for x,y in ranges]
