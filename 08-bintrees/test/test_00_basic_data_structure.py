import pytest

from bintree import BinaryTreeNode


def test_single_node_is_leaf():
    single_node = BinaryTreeNode('a')
    assert single_node.is_leaf()


def test_left_2(all_left_tree_2):
    assert not all_left_tree_2.is_leaf()


def test_null_node():
    null_node = BinaryTreeNode(None)
    assert null_node.is_leaf()


def test_left_is_a_binary_treenode():
    top_node = BinaryTreeNode('a')
    with pytest.raises(ValueError):
        top_node.left = None


def test_right_is_a_binary_treenode():
    top_node = BinaryTreeNode('a')
    with pytest.raises(ValueError):
        top_node.right = None
