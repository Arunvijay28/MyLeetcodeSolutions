def findMaxAverage(self, nums, k: int) -> float:
        curr=maxsum=sum(nums[:k])

        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]         # sliding window add the right element ,subract the left element
            maxsum=max(maxsum,curr)
        return maxsum/k


# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000