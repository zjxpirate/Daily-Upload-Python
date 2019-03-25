
import collections
import functools

from Binary_Trees_utils import must_find_node, strip_parent_link

from Binary_Trees_node import BinaryTreeNode



def lca(tree, node0, node1):

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes +
            (node0, node1).count(tree))
        return Status(num_target_nodes, tree
                      if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor




b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))

c1 = BinaryTreeNode(2)
c2 = BinaryTreeNode(4)

print(lca(b, c1, c2))


