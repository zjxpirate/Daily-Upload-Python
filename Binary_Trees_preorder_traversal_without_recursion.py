

#b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))
#b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))


from Binary_Trees_node import BinaryTreeNode



def preorder_traversal(tree):

    path, result = [tree], []
    print("path: ", path)
    while path:
        curr = path.pop()
        print("curr: ", curr)
        if curr:
            result.append(curr.data)
            print("result: ", result)
            path += [curr.right, curr.left]
            print("path: ", path)
            print("\n")
    print("\n")
    print("The result is below: ")
    return result




b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))

print(preorder_traversal(b))



