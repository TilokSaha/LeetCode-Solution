class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if mat == [] or r * c != len(mat) * len(mat[0]):  # <---- If the list doesnt satisfies the condition then we just return the matrix itself
            return mat
        
        A=[[0 for i in range(c)] for i in range(r)]  # <--------- Creating a list with the defined rows and columns
        k=0       # <------------- linear counter 
        for i in mat:      # <------ Traversing each elements
            for j in i:
                A [ k // c ] [ k % c ] = j   # <------ Putting each elements in the new array with new dimension
                k=k+1
        return A      # <----- Returning the new array