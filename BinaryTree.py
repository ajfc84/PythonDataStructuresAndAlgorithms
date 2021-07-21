
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.left_child = leftChild
newBT.right_child = rightChild


def preorder_traversal(root):
    if not root:
        return
    print(root.data)
    preorder_traversal(root.left_child)
    preorder_traversal(root.right_child)


preorder_traversal(newBT)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left_child)
    print(root.data)
    inorder_traversal(root.right_child)


inorder_traversal(newBT)


def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left_child)
    postorder_traversal(root.right_child)
    print(root.data)


postorder_traversal(newBT)


