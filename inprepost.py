# Tree traversal in Python


class Nodes:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.value = item
def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.value) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.value) + "->",end='')


def preorder(root):
    if root:
        # Traverse root
        print(str(root.value) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Nodes(1)
root.left = Nodes(2)
root.right = Nodes(3)
root.left.left = Nodes(4)
root.left.right = Nodes(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
