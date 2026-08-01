class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        left = 0
        hash_set = set()
        longest_substring = 0

        for right in range(len(s)):

            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            
            hash_set.add(s[right])
            
            current_length = right - left + 1
            longest_substring = max(current_length, longest_substring)
        
        return longest_substring