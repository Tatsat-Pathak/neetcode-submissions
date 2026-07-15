class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_num = max(nums)

        if max_num < 0:
            return 1
        
        for value in range(1, max_num + 1):

            if value not in nums:
                return value
        
        return max_num + 1