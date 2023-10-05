import pytest

from bintree import BinaryTreeNode


def test_height_of_one():
    result = BinaryTreeNode('a').height
    assert result == 1


def test_two_level_tree(all_left_tree_2):
    assert all_left_tree_2.height == 3
