#Given a binary tree root, check if it's symmetric around its center (a mirror of itself)

class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and \
               is_mirror(t1.left, t2.right) and \
               is_mirror(t1.right, t2.left)
    
    return is_mirror(root.left, root.right)

# Example usage:
# Symmetric tree:
#       1
#     /   \
#    2     2
#   / \   / \
#  3  4  4  3

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

print(is_symmetric(root))  