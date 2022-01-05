class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A=[]   # <----- Taking an empty array
        for i in range(numRows):    # <------ initializing each element of the pascals triangle with 1
            A.append([1]*(i+1))     
        for i in range(2,numRows):   # <----- Starting from third row because its already complete no need to change anything
            for j in range(1,len(A[i])-1):   
                A[i][j]=A[i-1][j-1]+A[i-1][j]      # <----- Adding previous elements from the above list 
        return A      # <--- Returning the result