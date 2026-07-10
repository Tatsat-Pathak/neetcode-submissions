class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        temp = []
        for value in nums:
            if value == val:
                temp.append(value)
            else:
                nums[k] = value
                k += 1
        
        return k