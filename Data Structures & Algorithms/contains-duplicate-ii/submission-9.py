class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        size = len(nums) - 1

        while i < size:
            if nums[i] == nums[j]:
                if abs(i - j) <= k:
                    return True 
            
            if j == size:
                i += 1
                j = i + 1
                continue
            
            j += 1
        
        return False