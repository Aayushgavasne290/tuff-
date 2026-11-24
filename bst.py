# Step 1: Same TreeNode class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#    Step 2: Insert a number using the BST rule
def insert(root, value):
    # If we hit an empty spot, put the new node here
    if root is None:
        return TreeNode(value)

    if value < root.data:
        root.left = insert(root.left, value)    # Go left if smaller
    else:
        root.right = insert(root.right, value)  # Go right if bigger

    return root

# Step 3: Search for a number
def search(root, target):
    if root is None:
        return False           # Reached dead end, not found
    if root.data == target:
        return True            # Found it!

    if target < root.data:
        return search(root.left, target)   # Look in left side
    else:
        return search(root.right, target)  # Look in right side

# Step 4: Inorder Traversal (Left -> Print -> Right)
def show_sorted(root):
    if root is not None:
        show_sorted(root.left)
        print(root.data, end=" ")
        show_sorted(root.right)

# Step 5: Test it
root = None
for num in [50, 30, 70, 20, 40]:
    root = insert(root, num)

print("Sorted tree:", end=" ")
show_sorted(root)                      # Output: 20 30 40 50 70
print("\nIs 40 in tree?", search(root, 40))  # Output: True
print("Is 99 in tree?", search(root, 99))    # Output: False