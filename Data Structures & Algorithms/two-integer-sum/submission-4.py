class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j, value in enumerate(nums):
            other = target - value
            
            if other in seen:
                i = seen[other]
                return [i, j]

            seen[value] = j