from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_binary_tree(array: list) -> TreeNode:
    def get_node(index):
        if index >= len(array) or array[index] is None:
            return None

        node = TreeNode(
            val=array[index],
            left=get_node((index + 1) * 2 - 1),
            right=get_node((index + 1) * 2)
        )

        return node

    return get_node(0)


def print_tree(root: Optional[TreeNode], depth=0):
    if root is None:
        return

    print('  ' * depth + str(root.val))

    print_tree(root.left, depth + 1)
    print_tree(root.right, depth + 1)
