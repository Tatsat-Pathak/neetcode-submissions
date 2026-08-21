class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for bracket in s:

            if bracket in '({[':
                stack.append(bracket)
            
            if bracket in ')}]':
                if not stack or stack[-1] != brackets[bracket]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0