
from bstNode import BstNode, insert
import collections


tree_1 = BstNode(19, None, None)

insert(7, tree_1)
insert(43, tree_1)
insert(3, tree_1)
insert(11, tree_1)
insert(23, tree_1)
insert(47, tree_1)
insert(2, tree_1)
insert(5, tree_1)
insert(17, tree_1)
insert(37, tree_1)
insert(53, tree_1)
insert(13, tree_1)
insert(29, tree_1)
insert(41, tree_1)
insert(31, tree_1)




# 14. the range lookup problem

Interval = collections.namedtuple('Interval', ('left', 'right'))

int = Interval(left=16, right=31)

def range_lookup_in_bst(tree, interval):

    def range_lookup_in_bst_helper(tree):

        if tree is None:
            return

        if interval.left <= tree.data <= interval.right:
            # tree.data lies in the interval.
            range_lookup_in_bst_helper(tree.left)
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)

        elif interval.left > tree.data:
            range_lookup_in_bst_helper(tree.right)

        else:  # interval.right > tree.data
            range_lookup_in_bst_helper(tree.left)


    result = []
    range_lookup_in_bst_helper(tree)
    return result

print(range_lookup_in_bst(tree_1, int))























