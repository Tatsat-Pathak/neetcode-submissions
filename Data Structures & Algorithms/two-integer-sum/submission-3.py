class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            other = target - value
            print(f"need : {other}")
            if other in nums[i + 1:]:
                j = nums.index(other, i + 1)
                if nums[i] + nums[j] == target:
                    return [i, j]