class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D={}     # <-----Using HashMap,by storing the elements:index pair that we have already traversed 
        for i in range(len(nums)):   # <---- Traversing each element with O(n) Time complexity
            if target-nums[i] in D:      # <----- if the other part of the sum is already present in the hashmap we return the indices and stop any further execution
                return D[target-nums[i]],i
            D[nums[i]]=i  # <--- if not then we keep adding the elements in the hashmap