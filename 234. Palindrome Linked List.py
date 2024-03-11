class Solution:
    def isPalindrome(self, head) -> bool:
        s=""
        temp=head
        while temp:
            s+=str(temp.val)
            temp=temp.next
        return s==s[::-1]
    

# Input: head = [1,2,2,1]
# Output: true