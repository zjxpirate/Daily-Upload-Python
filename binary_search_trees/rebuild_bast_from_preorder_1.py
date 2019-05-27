
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
    if not preorder_sequence:
        return None

    transition_point = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

    print(transition_point)

    return BstNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:transition_point]), rebuild_bst_from_preorder(preorder_sequence[transition_point:]))

print(rebuild_bst_from_preorder(pre_seq))
















