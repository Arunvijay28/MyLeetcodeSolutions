def findRelativeRanks(self, score) :
        # score.sort(reverse=True)
        d =dict(int)
        nums=score
        place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(nums)
        a = [" "]*n
        for i in range(n): d[nums[i]] = i
        nums.sort(reverse=True)

        for i in range(n):
            if i < 3:
                a[d[nums[i]]] = place[i]            
            else:
                a[d[nums[i]]] = str(i+1)
                
        return a 

# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].