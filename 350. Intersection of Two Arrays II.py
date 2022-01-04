class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A=[]                           # <----- Empty for storing the elements occuring in both list
        for i,n in enumerate(nums1):    # <------ Traversing through the first list
            if n in nums2:               # <------- if the element is present the second list
                A.append(n)               # <------- Then we append to our define list A
                nums2.remove(n)            # <------- And remove the element because its job is already done 
        return A            # <----- returning the elements that we have stored so far