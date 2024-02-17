def hammingDistance(self, x: int, y: int) -> int:
        sx=""
        while x:
            sx+=str(x%2)
            x=x//2
        sy=""
        while y:
            sy+=str(y%2)
            y=y//2
        if len(sx)>len(sy):
            sy+='0'*(len(sx)-len(sy))
        else:
            sx+='0'*(len(sy)-len(sx))
        sx[::-1]
        sy[::-1]
        dist=0
        for i in range(len(sx)):
            if sx[i]!=sy[i]:
                dist+=1
        return dist



# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:

# Input: x = 3, y = 1
# Output: 1

