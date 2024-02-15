def pascal(numRows):
        result=[]
        if numRows==0:
            return result
        l1=[1]
        result.append(l1)
        for i in range(1,numRows):
            prow=result[i-1]
            current=[1]

            for j in range(1,i):
                current.append(prow[j]+prow[j-1])
            current.append(1)

            result.append(current)
        return result


# returns the pascal triangle of given no of rows