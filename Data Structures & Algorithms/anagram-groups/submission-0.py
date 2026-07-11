class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = {}
        for value in strs:
            key = "".join(sorted(value))

            if key not in anagrams_groups:
                anagrams_groups[key] = []
            
            anagrams_groups[key].append(value)

        return list(anagrams_groups.values())