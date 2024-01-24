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


def print_tree(root: TreeNode, depth=0):
    if root is None:
        return

    print('  ' * depth + str(root.val))

    print_tree(root.left, depth + 1)
    print_tree(root.right, depth + 1)


class Solution(object):
    def find_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.find_depth(root.left)
        right = self.find_depth(root.right)

        return 1 + max(left, right)

    def depth_first_search(self, root: TreeNode, curr: int, depth: int):
        if root is None:
            return None

        if curr == depth:
            return root

        left = self.depth_first_search(root.left, curr + 1, depth)
        right = self.depth_first_search(root.right, curr + 1, depth)

        if left and right:
            return root

        return left if left else right

    def lca_deepest_leaves(self, root: TreeNode):
        """
        Lowest common ancestor of deepest leaves
        """
        if root is None:
            return None

        depth = self.find_depth(root) - 1

        return self.depth_first_search(root, 0, depth)


if __name__ == '__main__':
    tests = [
        array_to_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
        array_to_binary_tree([1]),
        array_to_binary_tree([0, 1, 3, None, 2]),
        array_to_binary_tree([0, 1, None, 3, None, None, None, 7, 8])
    ]

    for test in tests:
        print('--------- input')

        print_tree(test)

        print('--------- output')

        solution = Solution()
        print_tree(solution.lca_deepest_leaves(test))
