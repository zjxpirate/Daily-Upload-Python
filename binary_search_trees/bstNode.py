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





