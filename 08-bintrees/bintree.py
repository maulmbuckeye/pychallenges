class BinaryTreeNode:
    def __init__(self, item):
        if item is not None:
            self.left = BinaryTreeNode(None)
            self.right = BinaryTreeNode(None)
        self.item = item

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return f"BinaryTreeNode [{self.item=}, {self.left=}, {self.right=}]"

    def traverse(self, ttype):
        if self.item is None:
            return []

        the_list = []
        the_list += [self.item] if ttype == "pre" else []
        the_list += self.left.traverse(ttype)
        the_list += [self.item] if ttype == "in" else []
        the_list += self.right.traverse(ttype)
        the_list += [self.item] if ttype == "post" else []

        return the_list

    def inorder(self):
        return self.traverse("in")

    def preorder(self):
        return self.traverse("pre")

    def postorder(self):
        return self.traverse("post")

    @property
    def height(self):
        if self.item is None:
            return 0
        return max(self.left.height, self.right.height) + 1
