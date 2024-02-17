def intersect(self, nums1 ,nums2):
        nums1.sort()
        nums2.sort()
        il=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                il.append(nums1[i])
                i+=1
                j+=1
        return il


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# input : num1=[1,2],num2=[1,1]
# output: [1] not [1,1]