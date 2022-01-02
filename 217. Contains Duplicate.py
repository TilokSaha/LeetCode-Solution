class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

        # Normal Solution
        # if len(set(nums))==len(nums):   # <--- Just comparing the number of element present in the list vs its set
        #     return False
        # else:
        #     return True
        
        #Using HashMap
        s=set()    # <--  Storing the elements that we have already traversed
        for i in nums:   # <-- Going through each elements
            if i in s:
                return True    # <-- If an element is fount in the set, then we return True
            s.add(i)          # <--- If not then we just keep updating our set with new element
        return False   # <--- If there is no trigger in the entire list, then we return False