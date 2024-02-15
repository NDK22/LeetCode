class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_list = [num for num in nums if num > 0]
        negative_list = [num for num in nums if num < 0]
        output =[]
        for postive, negative in zip(positive_list,negative_list):
            output.extend([postive,negative])
        return output
