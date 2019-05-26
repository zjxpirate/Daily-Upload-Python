
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



# 6. find the k largest elements in a bst

def find_k_largest_in_bst(tree, k):

    def find_k_largest_in_bst_helper(tree):

        # perform reverse inorder traversal
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)

            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)

                print("k_largest_elements: ", k_largest_elements)

                find_k_largest_in_bst_helper(tree.left)


    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


print(find_k_largest_in_bst(tree_1, 5))





















