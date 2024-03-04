def hasAlternatingBits(self, n: int) -> bool:
        bit=""
        while n:
            bit+=str(n%2)
            n=n//2
        bit[::-1]
        for i in range(len(bit)-1):
            if bit[i]==bit[i+1]:
                return False
        return True


# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101

# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.

# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.