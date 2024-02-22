class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target not in nums:
        #     nums.append(target)
        #     nums.sort()
        # for i, number in enumerate(nums):
        #     if number == target:
        #         return i

        left , right = 0, len(nums) -1 
        while left <= right:
            mid = left + (right -left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid +1
            else:
                right = mid -1
        return left
