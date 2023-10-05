import pytest

from bintree import BinaryTreeNode


@pytest.fixture()
def all_left_tree_2():
    top = BinaryTreeNode('a')
    top.left = BinaryTreeNode('b')
    top.left.left = BinaryTreeNode('c')

    return top
