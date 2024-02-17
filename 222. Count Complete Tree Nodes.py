def countNodes(self, root) -> int:
        if root is None:
            return 0
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1