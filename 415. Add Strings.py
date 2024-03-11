def addStrings(self, num1: str, num2: str) -> str:
        d={'1':1,'2':2,'3':3,'4':4,'5':5,
            '6':6,'7':7,'8':8,'9':9,'0':0}
        n1=0
        n2=0
        if len(num2)>30:
            return str(int(num1)+int(num2))
        else:
            for i in num1:
                n1=n1*10+d[i]
            for i in num2:
                n2=n2*10+d[i]
            return f"{n1+n2}"


# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"~
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"