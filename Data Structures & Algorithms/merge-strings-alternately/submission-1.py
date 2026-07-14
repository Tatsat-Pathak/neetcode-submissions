class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = []
        
        word1_length = len(word1)
        word2_length = len(word2)
        index = 0

        while index < word1_length or index < word2_length:

            if index >= word1_length:
                merge_string.append(word2[index:])
                break

            if index >= word2_length:
                merge_string.append(word1[index:])
                break

            merge_string.append(word1[index])
            merge_string.append(word2[index])
            index += 1
        
        merge_string = "".join(merge_string)

        return merge_string