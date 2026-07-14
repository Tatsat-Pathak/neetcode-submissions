class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = []
        
        word1_length = len(word1)
        word2_length = len(word2)
        index = 0

        while index < word1_length and index < word2_length:

            merge_string.extend([word1[index], word2[index]])
            index += 1
        
        if index > word1_length - 1:
            merge_string.append(word2[index:])

        if index > word2_length - 1:
            merge_string.append(word1[index:])

        return "".join(merge_string)