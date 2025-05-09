class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        tri = [] #  Initialize an empty list to store rows 

        for i in range(rowIndex + 1): # since rowIndex is 0-based
            row = [1] * (i+1) # Start with a row filled with 1's

            for j in range(i):

                if j != 0:  # Update the inner values of the row 
                    row[j] = tri[i - 1][j - 1] + tri[i - 1][j] # # update them based on the sum of the two values directly above from the previous row.

            tri.append(row) # Append the each newly computed row to tri

        return tri[rowIndex]
