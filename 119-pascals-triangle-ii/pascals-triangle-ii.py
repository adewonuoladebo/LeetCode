class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            mother_row = [1,2,1] #the preceeding row
            next_row = []
            for j in range(len(mother_row)+1): #create the next row by initializing it with 1's at the ends and 0's in between. the 0's are placeholders
                next_row.append(0)
            next_row[0] = 1
            next_row[-1] = 1
            
            
            for x in range(rowIndex-2): #noticed based on observation - this prompts us to recalculate next_row when we're not at the level rowIndex dictates
                
                for k in range(1,len(mother_row)):
                    next_row[k] = mother_row[k-1] + mother_row[k] #updates next row based on values in the mother row

                
                if len(next_row) != rowIndex + 1: #if next row is not the desired length with the right values i.e the numbers at the level of the triangle we want
                    mother_row = next_row #set the mother row to what next row is
                    next_row = [] #reset next_row to the [1, 0, 0, ....., 0,1] format 
                    for l in range(len(mother_row)+1): #
                        next_row.append(0)
                    next_row[0] = 1
                    next_row[-1] = 1   
        
    
        return next_row
    