class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        # M = float('-inf')    # <--- Default Lowest Value
        # for i in range(len(nums)): # <-- Applying Brute-Force Method, just for demonstration (Time Limite Exceeded for this algorithm)
        #     S = 0 # <--- Getting the sum 
        #     for j in range(i,len(nums)):  # <--- Findning every Possible Group of segment of the array
        #         S=S+nums[j]    # <---- Getting the sum of those groups
        #         M = max (M,S)    # <------ Comparing whether the intial sum was greater or the new sum of the group is greater
                
        # return M   # <--- returning the greatest sum 

        A=nums.copy()
        for i in range(1,len(nums)):   # <--- Kadane's Algorithm
            if A[i-1]>0:              # <--- We are keep adding the next element if the sum of the previous group is positive, if its negative we break the chain and start new series of sum
                A[i]=A[i-1]+A[i]     # <--- We are also storing the intermediate sum
        return max(A)               # <---- And returning the largest sum in the series


        # M=float('-inf')                     # <---- Modified version of Kadane's Algorithm
        # S=0                                # <----- Space Complexity is O(1) since we are not storing in an array
        # for i in range(len(nums)):
        #     S=max(S+nums[i],nums[i])       # <------We are keep on adding until we hit a point where the previous sum is negative and we continue with a new series
        #     M=max(S,M)                      # <-----Storing the maximum Value
        # return M