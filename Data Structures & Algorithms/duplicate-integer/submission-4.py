class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        
        for value in nums:
            count = nums.count(value)
            if count > 1:
                return True
            
        return False