def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        front=0
        end=len(s)-1
        while front <= end:
            s[front],s[end]=s[end],s[front]
            front+=1
            end-=1



# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]