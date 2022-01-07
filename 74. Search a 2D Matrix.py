class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix:
        #     if target in i:
        #         return True      # <--------- if the target is present in any of the row then we return True
        # return False
        
        if not matrix or not matrix[0]: 
            return False
        m,n=len(matrix[0]),len(matrix)
        beg,end = 0,m*n-1    # <--------- total number of element - 1
        
        while beg < end:            # <------ for larger value we would apply binary search for optimizaion
            
            mid = (beg + end)//2  # <------ getting the mid value
        
            if matrix[mid//m][mid%m] < target:
                beg = mid+1     # <--------- if the element is in the first half
            else:
                end = mid       # <-------- if the element is in the second half
        return matrix[beg//m][beg%m] == target   # <--------returning whether we found the element or not
                