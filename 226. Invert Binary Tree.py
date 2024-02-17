def invertTree(self, root):
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root



# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Input: root = [2,1,3]
# Output: [2,3,1]


# Input: root = []
# Output: []