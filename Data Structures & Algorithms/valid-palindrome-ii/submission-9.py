class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_palindrome(start, end):
            
            while start < end:

                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True
        
        while left < right:
            
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
                
            left += 1
            right -= 1
        
        return True