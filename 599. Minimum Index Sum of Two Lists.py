def findRestaurant(self, list1, list2):
        dic={}
        c=0
        if len(list1)>len(list2):
            min_len=len(list2)
            c=1
        else:
            min_len=len(list1)
        
        if c==0:
            for i in list1:
                if i in list2:
                    x=list1.index(i)
                    y=list2.index(i)
                    dic[i]=x+y
        else:
            for i in list2:
                if i in list1:
                    x=list1.index(i)
                    y=list2.index(i)
                    dic[i]=x+y
        min_val=min(dic.values())
        ans=[key for key,value in dic.items() if value==min_val]
        return ans


# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

# Example 3:

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".