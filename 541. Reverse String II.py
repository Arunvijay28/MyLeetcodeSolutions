def reverseStr(self, s: str, k: int) -> str:
        rev=""
        if len(s)<k:
            return s[::-1]
        if len(s)<2*k or len(s)==k:
            a=s[0:k]
            rev=a[::-1]+s[k:]
            return rev
        for i in range(0,len(s),2*k):
            a=s[i:k+i]
            rev=rev[0:i]+a[::-1]+s[k+i:]
        return rev



# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"