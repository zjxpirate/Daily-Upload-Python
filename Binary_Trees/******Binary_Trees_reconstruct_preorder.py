


from Binary_Trees_node import BinaryTreeNode
import functools


def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)

        if subtree_key is None:
            return None


        # Note that reconstruct_preorder_helper updates preorder_iter. So the order
        # of following two calls are critical.

        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)

        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)


    return reconstruct_preorder_helper(iter(preorder))





def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))






preorder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']


print(reconstruct_preorder_wrapper(executor, preorder))