class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = m
        index_2 = 0

        while index_1 < len(nums1):

            nums1[index_1] = nums2[index_2]
            index_1 += 1
            index_2 += 1

        return nums1.sort()