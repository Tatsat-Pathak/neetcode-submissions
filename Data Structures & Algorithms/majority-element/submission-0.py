class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = len(nums) / 2
        distinct_elements = set(nums)

        for value in distinct_elements:
            
            element_count = nums.count(value)
            if element_count > majority:
                return value