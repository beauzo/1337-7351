from typing import Optional
import tree_node


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


class Solution(object):
    def find_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.find_depth(root.left)
        right = self.find_depth(root.right)

        return 1 + max(left, right)

    def depth_first_search(self, root: Optional[TreeNode], curr: int, depth: int) -> Optional[TreeNode]:
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


class Solution2:
    def lca(self, root, p, q):
        if root in (None, p, q):
            return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)
        return root if l and r else l or r

    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []

        def dfs(node, h):
            if not node:
                return
            if len(a) == h:
                a.append([])
            a[h].append(node)
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)

        dfs(root, 0)

        p, q = a[-1][0], a[-1][-1]
        return self.lca(root, p, q)


class Solution3:
    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            l, r = dfs(node.left), dfs(node.right)
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            if l[0] < r[0]:
                return r[0] + 1, r[1]
            return l[0] + 1, node

        return dfs(root)[1]


if __name__ == '__main__':
    tests = [
        array_to_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
        array_to_binary_tree([1]),
        array_to_binary_tree([0, 1, 3, None, 2]),
        array_to_binary_tree([0, 1, None, 3, None, None, None, 7, 8])
    ]

    for t in tests:
        print('--------- input')

        print_tree(t)

        print('--------- output')

        solution = Solution()
        print_tree(solution.lca_deepest_leaves(t))
        solution2 = Solution2()
        print_tree(solution2.lca_deepest_leaves(t))
        solution3 = Solution3()
        print_tree(solution3.lca_deepest_leaves(t))
