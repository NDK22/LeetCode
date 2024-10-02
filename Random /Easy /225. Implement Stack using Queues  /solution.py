class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map={}
        for i, number in enumerate(nums):
            if number in hash_map and abs(i-hash_map[number])<=k:
                return True
            else:
                hash_map[number]=i
        return False 
