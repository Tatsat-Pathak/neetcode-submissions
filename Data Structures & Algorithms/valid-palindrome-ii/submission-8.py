class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_palindrome(string):
            
            return string == string[::-1]
        
        while left < right:
            
            if s[left] != s[right]:
                return is_palindrome(s[left + 1 : right + 1]) or is_palindrome(s[left : right])
                
            left += 1
            right -= 1
        
        return True