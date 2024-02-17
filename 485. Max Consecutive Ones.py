def findMaxConsecutiveOnes(self, nums) -> int:
        count=0
        l=[]
        for i in nums:
            if i!=1:
                l.append(count)
                count=0
            else:
                count+=1
        l.append(count)
        print(l)
        return max(l)

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2