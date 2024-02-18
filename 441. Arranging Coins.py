def arrangeCoins(self, n: int) -> int:
        i=0
        while n>=0:
            i=i+1
            n=n-i
        return i-1


# maths: return int(math.sqrt((1+8*n)-1)/2) 0ms