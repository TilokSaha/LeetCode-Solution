class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1         # <----- Last index for the first list
        j = n-1         # <----- Last index for the second list
        k = m+n-1       # <----- Last index for the combination of both the list
        
        while j>=0:          # <---- looping until the the second list is empty
            if i>=0 and nums1[i]>nums2[j]:  # <---- checking whether the last element of the first is greater than the second 
                nums1[k]=nums1[i]          # <---- if thats true we assign the last element of the combined list with the last element of the first list
                k-=1                      # <---- moving towards the previous element of the combined list
                i-=1                     # <---- moving towards the previous element of the first list
            else:
                nums1[k]=nums2[j]        # <---- else we do it with the second list instead
                k -= 1                    # <---- previous element of the combined
                j -= 1                     # <---- previous element of the second