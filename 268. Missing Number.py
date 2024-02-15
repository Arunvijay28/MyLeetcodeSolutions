def missingNumber(self, nums) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i



# missing no in range [0,n]
            