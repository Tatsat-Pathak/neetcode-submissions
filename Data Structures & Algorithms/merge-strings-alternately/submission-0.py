class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = ""
        
        word1_length = len(word1)
        word2_length = len(word2)
        index = 0

        while word1_length or word2_length:

            if word1_length == 0:
                merge_string += word2[index : ]
                break

            if word2_length == 0:
                merge_string += word1[index :]
                break
            
            merge_string += word1[index] + word2[index]

            word2_length -= 1
            word1_length -= 1
            index += 1
        
        return merge_string