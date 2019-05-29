
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

t0 = tree_1                      #19
print(t0)

mm = tree_1.right.left           #23
print(mm)

t1 = tree_1.right.left.right     #37
print(t1)



# 13. test if bst nodes are totally ordered

def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0, possible_anc_or_desc_1, middle):

    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1

    # perform interleaved searching from possible_anc_or_desc_0 and possible_anc_or_desc_1 for middle.

    while (search_0 is not possible_anc_or_desc_1 and search_0 is not middle and search_1 is not possible_anc_or_desc_0 and search_1 is not middle and (search_0 or search_1)):

        if search_0:
            search_0 = (search_0.left if search_0.data > middle.data else search_0.right)

        if search_1:
            search_1 = (search_1.left if search_1.data > middle.data else search_1.right)


    # if both searches were successful, or we got from possible_anc_or_desc_0 to possible_anc_or_desc_1
    # without seeing middle, or from possible_anc_or_desc_1 to possible_anc_or_desc_0 without seeing middle,
    # middle cannot lie between possible_anc_or_desc_0 and possible_anc_or_desc_1.

    if ((search_0 is not middle and search_1 is not middle) or search_0 is possible_anc_or_desc_1 or search_1 is possible_anc_or_desc_0):
        return False


    def search_target(source, target):

        while source and source is not target:
            source = source.left if source.data > target.data else source.right
        return source is target

    # if we get here, we already know one of possible_anc_or_desc_0 or possible_anc_or_desc_1 has a path to
    # middle. check if middle has a path to possible_anc_or_desc_1 or to possible_anc_or_desc_0.

    return search_target(middle, possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0)


print(pair_includes_ancestor_and_descendant_of_m(t0, t1, mm))



























