from bintree import BinaryTreeNode



def create_book_example_tree():
    top = BinaryTreeNode('d4')

    top.left = BinaryTreeNode('b2')
    top.left.left = BinaryTreeNode('a1')
    top.left.right = BinaryTreeNode('c3')

    top.right = BinaryTreeNode('f6')
    top.right.left = BinaryTreeNode('e5')
    top.right.right = BinaryTreeNode('g7')

    return top

def all_left_tree_2():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    top.left.left = BinaryTreeNode('c')

    return top


def test_empty_node():
    assert BinaryTreeNode(None).inorder() == []

def test_only_top():
    a_list = BinaryTreeNode('a').inorder()
    assert a_list == ['a']


def test_two_left_leaves():
    top = all_left_tree_2()

    assert top.inorder() == ['c', 'b', 'a']


def test_two_right_leaves():
    top = BinaryTreeNode('a')
    top.right = BinaryTreeNode('e')
    top.right.right = BinaryTreeNode('f')

    assert top.inorder() == ['a', 'e', 'f']




def test_book_example_of_inorder():
    result = create_book_example_tree().inorder()
    book_to_list = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7']
    assert result == book_to_list


def test_book_example_of_preorder():
    result = create_book_example_tree().preorder()
    book_to_prelist = ['d4', 'b2', 'a1', 'c3', 'f6', 'e5', 'g7']
    assert result == book_to_prelist


def test_book_example_of_postorder():
    result = create_book_example_tree().postorder()
    book_to_postlist = ['a1', 'c3', 'b2', 'e5', 'g7', 'f6', 'd4']
    assert result == book_to_postlist


def test_height_of_one():
    result = BinaryTreeNode('a').height
    assert result == 1


def test_two_level_tree():
    top = all_left_tree_2()
    assert top.height == 3
