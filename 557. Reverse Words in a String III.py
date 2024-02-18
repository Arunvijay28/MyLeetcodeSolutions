def reverseWords(self, s: str) -> str:
        rev=""
        a=s.split()
        for i in a:
            rev+=i[::-1]+" "
        return rev[0:len(rev)-1]


# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"