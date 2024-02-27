def maximumProduct(self, nums) -> int:
        nums.sort()
        # print(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])


# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6

### input=[-100,-98,-1,2,3,4]
### output :39200