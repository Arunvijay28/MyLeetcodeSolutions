def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        st=""
        s=s[::-1]
        for i in range(0,len(s),k):
            st+=s[i:i+k]
            st+="-"
        st=st[::-1]
        return st.replace("-","",1)



# Example 1:

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.

# Example 2:

# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.