class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        size = len(nums)
        triplets = []
        for i in range(size - 2):
            j = i + 1
            k = size - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                if sums == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
                elif sums < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return triplets