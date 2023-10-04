from bintree import BinaryTreeNode
import pytest


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


def test_find_lca_just_top():
    lca = BinaryTreeNode('a').find_lca('a', 'a')
    assert lca == 'a'


def test_find_lca_just_top_not_there():
    lca = BinaryTreeNode('a').find_lca('a', 'b')
    assert lca is None


def test_find_lca_in_two_nodes():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    lca = top.find_lca('a', 'b')
    assert lca == 'a'


def test_find_lca_in_three_nodes():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    top.right = BinaryTreeNode('c')
    lca = top.find_lca('c', 'b')
    assert lca == 'a'


def test_second_level_is_lca():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    top.left.left = BinaryTreeNode('d')
    top.right = BinaryTreeNode('c')
    lca = top.find_lca('d', 'b')

    assert lca == 'b'


def test_second_level_on_right_is_lca():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    top.left.left = BinaryTreeNode('d')
    top.right = BinaryTreeNode('c')
    top.right.right = BinaryTreeNode('f')
    lca = top.find_lca('c', 'f')

    assert lca == 'c'


def set_up_book_example():
    top = BinaryTreeNode(6)
    top.left = BinaryTreeNode(4)
    top.left.left = BinaryTreeNode(2)
    top.left.right = BinaryTreeNode(5)
    top.left.left.left = BinaryTreeNode(1)
    top.left.left.right = BinaryTreeNode(3)
    top.right = BinaryTreeNode(7)
    top.right.right = BinaryTreeNode(10)

    return top


top = set_up_book_example()


def test_book_example():

    lca = top.find_lca(1, 5)
    assert lca == 4


@pytest.mark.parametrize("v1, v2, expected",
                         [(1, 3, 2), (1, 5, 4), (2, 5, 4), (3, 5, 4), (1, 7, 6)])
def test_book_example_param(v1, v2, expected):

    lca = top.find_lca(v1, v2)
    assert lca == expected
