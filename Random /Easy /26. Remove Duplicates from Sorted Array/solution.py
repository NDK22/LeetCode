class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j+=1
        nums[j] = nums[n-1]
        return j+1   
