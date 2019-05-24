

# 1. binary search tree boot camp

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





# 2. search binary search tree

def search_bst(tree, key):
    return (tree if not tree or tree.data == key else search_bst(tree.left, key)
            if key < tree.data else search_bst(tree.right, key))

#print(search_bst(tree_1, 53))





# 3. binary search tree libraries

import bintrees

t = bintrees.RBTree([(5, 'Alfa'), (2, 'Bravo'), (7, 'Charlie'), (3, 'Delta'), (6, 'Echo')])

print(t[2])

print(t.min_item(), t.max_item())

t.insert(9, 'Golf')

print(t)

print(t.min_key(), t.max_key())

t.discard(3)

print(t)

a = t.pop_min()

print(t)

b = t.pop_max()

print(t)















