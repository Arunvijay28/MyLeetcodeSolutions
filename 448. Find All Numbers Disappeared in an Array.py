def findDisappearedNumbers(self, nums):
        ret=[]
        nodup=set(nums)
        for i in range(1,len(nums)+1):
            if i not in nodup:
                ret.append(i)
        return ret


# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]
 