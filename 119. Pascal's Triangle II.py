def pascaltriangle(rowIndex):
        result=[]
        if rowIndex==0:
            return [1]
        
        firstrow=[1]
        result.append(firstrow)

        for i in range(1,rowIndex+1):
            prev=result[i-1]
            current=[1]

            for j in range(1,i):
                current.append(prev[j]+prev[j-1])
            
            current.append(1)
            result.append(current)
        return result[rowIndex]



# input: rowindex:3
# output: [1,3,3,1]