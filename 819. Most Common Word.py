def mostCommonWord(self, paragraph: str, banned) -> str:
        spc=''' !"'@#$%^&*()_+/{\|}'/.,<>:;?~` '''
        for i in spc:
            paragraph=paragraph.replace(i," ")
        l=paragraph.lower().split()
        print(l)
        dic={}
        for i in l:
            print(i)
            if i not in banned:
                if i not in spc:
                    dic[i]=l.count(i)
        val=max(dic,key=lambda x:dic[x])
        return val

''' another version'''

'''
def another_version(paragraph,banned):
    spc=" !?',.;"
    for i in spc:
        paragraph=paragraph.replace(i," ")  
        dic={}
        l=paragraph.lower().split()
        for i in l:
            if i not in banned:
                dic[i]=l.count(i)
        val=max(dic,key=lambda x:dic[x])
        return val

'''

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"