def isPalindrome(self, s: str) -> bool:
        sl=''' ,.`~!@#$%^&*()_+-=}[]{;'\:<>?'| " "'''
        if s==" ":
            return True
        else:
            old=""
            for i in s:
                if i not in sl:
                    old+=i
            print(old)
            new=""
            for i in range(1,len(old)+1):
                if old[-i] in sl:
                    continue
                else:
                    new+=old[-i]
            print(new)
            if old.lower()==new.lower():
                return True
            else:
                return False
            


# Example 1:
            
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 