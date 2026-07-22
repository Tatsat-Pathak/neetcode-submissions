class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        last_index = len(numbers) - 1
        total = numbers[index1] + numbers[index2]

        while total != target:

            if index1 < last_index and index2 == last_index:
                index2 = index1 + 1
                index1 += 1
            
            else:
                index2 += 1
            
            total = numbers[index1] + numbers[index2]
        
        return [index1 + 1, index2 + 1]