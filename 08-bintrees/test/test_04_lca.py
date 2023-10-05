import pytest

from bintree import BinaryTreeNode


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


@pytest.fixture()
def lca_book_example():
    top = BinaryTreeNode(6)
    top.left = BinaryTreeNode(4)
    top.left.left = BinaryTreeNode(2)
    top.left.right = BinaryTreeNode(5)
    top.left.left.left = BinaryTreeNode(1)
    top.left.left.right = BinaryTreeNode(3)
    top.right = BinaryTreeNode(7)
    top.right.right = BinaryTreeNode(10)

    return top


def test_book_example(lca_book_example):

    assert lca_book_example.find_lca(1, 5) == 4


@pytest.mark.parametrize("v1, v2, expected",
                         [(1, 3, 2), (1, 5, 4), (2, 5, 4), (3, 5, 4), (1, 7, 6)])
def test_book_example_param(v1, v2, expected, lca_book_example):
    assert lca_book_example.find_lca(v1, v2) == expected
