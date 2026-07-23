class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}

        for i in nums:
            if i not in freq_table:
                freq_table.update({i : 1})
                continue
            
            freq_table[i] += 1
        
        k_freq_element = sorted(freq_table, key = freq_table.get, reverse = True)

        return k_freq_element[:k]