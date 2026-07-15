class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        value = 1
        # if max_num < 0:
        #     return 1
        
        while True:

            if value not in nums:
                return value
            
            value += 1