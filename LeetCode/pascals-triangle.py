class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tri = [] # to store rows 

        for i in range(numRows):
            row = [1]*(i+1) # 1st all with 1

            for j in range(i): # can keep range(1,i)
                if j != 0 and j != -1: #  avoid changing ---------- 1
                                    #                             1  1
                                    #                            1      1
                                     #                         1          1
                                      #                      1              1
                    row[j] = tri[i-1][j-1] + tri[i-1][j]

            tri.append(row)

        return tri         
