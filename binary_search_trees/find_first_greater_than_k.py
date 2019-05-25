

class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({data!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({data!r}, {left!r})'
        else:
            fmt = '{}({data!r})'
        return fmt.format(type(self).__name__, **vars(self))


def insert(item, tree):
    if (item < tree.data):
        if (tree.left != None):
            insert(item, tree.left)
        else:
            tree.left = BstNode(item)
    else:
        if (tree.right != None):
            insert(item, tree.right)
        else:
            tree.right = BstNode(item)

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




# 5. find the first key greater than a value in bst

def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:  # root and all keys in left subtree are <= k, so skip them.
            subtree = subtree.right

    return first_so_far


print(find_first_greater_than_k(tree_1, 23))





