
from bstNode import BstNode, insert

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



# 8. reconstruct a bst from traversal data

pre_seq = [43, 23, 37, 29, 31, 41, 47, 53]

def rebuild_bst_from_preorder(preorder_sequence):

    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):

        if root_idx[0] == len(preorder_sequence):
            print("end\n")
            return None

        root = preorder_sequence[root_idx[0]]

        print("root: ", root)

        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1
        print("root_idx: ", root_idx[0])

        # note that rebuild_bst_from_preorder_on_value_range updates root_idx[0].
        # so the order of following two calls are critical.

        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        print("left_subtree: ", left_subtree)

        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)
        print("right_subtree: ", right_subtree)
        print("\n")
        return BstNode(root, left_subtree, right_subtree)


    root_idx = [0]

    print("hello\n")

    # tracks current subtree.
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))

print(rebuild_bst_from_preorder(pre_seq))












