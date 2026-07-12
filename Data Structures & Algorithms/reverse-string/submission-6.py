class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last = len(s) - 1
        i = 0
        j = last - i

        while i < j:

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j = last - i