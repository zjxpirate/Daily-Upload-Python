
from bstNode import BstNode

# 12. build a minimum height bst from a sorted array

list1 = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def build_min_height_bst_from_sorted_array(A):

    def build_min_height_bst_from_sorted_subarray(start, end):

        if start >= end:
            return None

        mid = (start + end) // 2

        return BstNode(A[mid], build_min_height_bst_from_sorted_subarray(start, mid), build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))

print(build_min_height_bst_from_sorted_array(list1))






























