class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        numRows = rowIndex + 1 #this code essentially builds off the code from Pascal's triangle 1

        #initializing empty Pascal's triangle
        for i in range(numRows):
            tri.append([]) 
            for x in range(i+1):
                tri[i].append(0)

     # we have [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]] at this stage

    
    #setting the digit of the first row and second row to 1
        if numRows >= 1:
            tri[0][0]= 1
        
    
    #setting the first and last digits in every row to 1 starting from row 3
        for j in range(1,numRows): 
            tri[j][0] = 1
            tri[j][-1] = 1
    # we have [[1], [1, 1], [1, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0, 1]] at this stage
            for k in range(1,j):
                tri[j][k] = tri[j-1][k-1] + tri[j-1][k]

        return tri[rowIndex]
    