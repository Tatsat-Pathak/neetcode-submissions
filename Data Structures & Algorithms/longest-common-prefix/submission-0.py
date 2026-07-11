class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key = len)
        longest_common_prefix = ""
        stop = False

        for index, value in enumerate(shortest_string):

            for i in range(len(strs)):

                if value != strs[i][index]:
                    stop = True
                    break

            else:
                longest_common_prefix += value 
            
            if stop:
                break
        
        return longest_common_prefix