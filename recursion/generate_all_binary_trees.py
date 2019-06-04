

import collections


def equal_binary_trees(node1, node2):
    if node1 and node2:
        return (node1.data == node2.data
                and equal_binary_trees(node1.left, node2.left)
                and equal_binary_trees(node1.right, node2.right))

    else:
        return not node1 and not node2




def binary_tree_to_string(tree):
    result = ''
    q = collections.deque()
    visited = set()
    first = True
    null_nodes_pending = 0

    result += '['
    q.append(tree)

    while q:
        node = q.popleft()
        if id(node) in visited:
            raise RuntimeError('Detected a cycle in the tree')
        if node:
            if first:
                first = False
            else:
                result += ', '

            while null_nodes_pending:
                result += 'null, '
                null_nodes_pending -= 1

            result += '"{}"'.format(node.data)

            visited.add(id(node))
            q.append(node.left)
            q.append(node.right)
        else:
            null_nodes_pending += 1

    result += ']'
    return result



class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()










# 12. generate binary trees

def generate_all_binary_trees(num_nodes):

    if num_nodes == 0:   # Empty tree, add as a None.
        return [None]

    result = []

    for num_left_tree_nodes in range(num_nodes):

        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes

        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)

        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)

        # generate all combinations of left_subtrees and right_subtrees.

        result += [BinaryTreeNode(0, left, right) for left in left_subtrees for right in right_subtrees]

    return result

print(generate_all_binary_trees(3))



