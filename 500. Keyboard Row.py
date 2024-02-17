def findWords(self, words):
        return [
            w
            for w in words
            if set(w.lower()).issubset(set("qwertyuiop"))
            or set(w.lower()).issubset(set("asdfghjkl"))
            or set(w.lower()).issubset(set("zxcvbnm"))
        ]


# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

# Example 2:

# Input: words = ["omk"]
# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]