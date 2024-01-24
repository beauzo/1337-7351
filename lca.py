from typing import Optional
from tree_node import TreeNode, array_to_binary_tree, print_tree


class Solution(object):
    def lowest_common_ancestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


if __name__ == '__main__':
    tests = [
        [array_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 8],
        [array_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 4],
        [array_to_binary_tree([2, 1]), 2, 1],
        [array_to_binary_tree([1]), 1, 1],
        [array_to_binary_tree([0, 1, 3, None, 2]), 3, 2],
        [array_to_binary_tree([0, 1, None, 3, None, None, None, 7, 8]), 0, 8],
        [array_to_binary_tree([8, 7, None, 5, None, None, None, 1, 0]), 0, 8]
    ]

    for test in tests:
        print('--------- input')

        print_tree(test[0])

        print('--------- output')

        solution = Solution()
        print_tree(solution.lowest_common_ancestor(test[0], test[1], test[2]))
