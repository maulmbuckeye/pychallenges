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

    def __repr__(self):
        return self.__str__()

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

    def find_lca(self, value1, value2):
        if not self.has_value(value1) or not self.has_value(value2):
            return None

        left_lca = self.left.find_lca(value1, value2)
        right_lca = self.right.find_lca(value1, value2)
        if not left_lca and not right_lca:
            return self.item
        if left_lca:
            return left_lca
        else:
            return right_lca

    def has_value(self, value):
        if self.item is None:

            return False
        if self.item == value:
            return True

        return (self.left.has_value(value) or
                self.right.has_value(value))
