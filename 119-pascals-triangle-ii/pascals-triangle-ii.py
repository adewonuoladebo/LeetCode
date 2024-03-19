class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            mother_row = [1,2,1]
            next_row = []
            for j in range(len(mother_row)+1): #create the next row
                next_row.append(0)
            next_row[0] = 1
            next_row[-1] = 1
            
            
            for x in range(rowIndex-2):
                
                for k in range(1,len(mother_row)):
                    next_row[k] = mother_row[k-1] + mother_row[k]

                
                if len(next_row) != rowIndex + 1:
                    mother_row = next_row #set the mother row to what next row is
                    next_row = [] #reset next_row to the [1, 0, 0, ....., 0,1] format 
                    for l in range(len(mother_row)+1): #
                        next_row.append(0)
                    next_row[0] = 1
                    next_row[-1] = 1   
        
    
        return next_row
    