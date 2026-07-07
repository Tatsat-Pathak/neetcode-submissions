class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        duplicate = set(nums)
        if len(duplicate) == size:
            return False
        
        return True