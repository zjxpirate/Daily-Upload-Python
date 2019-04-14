
import bisect, collections, math, operator, random


# # 1. Binary Search
# list1 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# def bsearch(t, A):
#     L, U = 0, len(A) - 1
#     while L <= U:
#         M = L + (U - L) // 2  # M = (L + U) // 2 will cause overflow
#         if A[M] < t:
#             L = M + 1
#         elif A[M] == t:
#             return M
#         else:
#             U = M - 1
#
#     return -1
#
# print(bsearch(9, list1))




# # 2. searching boot camp
#
# Student = collections.namedtuple('Student', ('name', 'grade_point_average'))
#
# def comp_gpa(student):
#     return(-student.grade_point_average, student.name)
#
#
# def search_student(students, target, comp_gpa):
#     i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
#     return 0 <= i < len(students) and students[i] == target




# # 3. Search a sorted array for first occurrence of K
#
# list2 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
#
# def search_first_of_k(A, k):
#     left, right, result = 0, len(A) - 1, -1
#     # A[left:right + 1] is the candidate set.
#     while left <= right:
#         mid = (left + right) // 2
#         if A[mid] > k:
#             right = mid - 1
#         elif A[mid] == k:   # nothing to the right of mid can be solution
#             result = mid
#             right = mid - 1
#         else:  # A[mid] < k
#             left = mid + 1
#
#     return result
#
# print(search_first_of_k(list2, 108))




# # 4. search entry equal to its index
#
# list3 = [-2, 0, 2, 3, 6, 7, 9]
#
# def search_entry_equal_to_its_index(A):
#     left, right = 0, len(A) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         difference = A[mid] - mid
#         # A[mid] == mid if and only if difference == 0.
#         if difference == 0:
#             return mid
#         elif difference > 0:
#             right = mid - 1
#         else:  # difference < 0
#             left = mid + 1
#
#     return -1
#
# print(search_entry_equal_to_its_index(list3))




# # 5. search smallest
#
# list4 = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
#
# def search_smallest(A):
#     left, right = 0, len(A) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if A[mid] > A[right]:
#             # minimum must be in A[mid + 1:right + 1].
#             left = mid + 1
#         else:  # A[mid] < A[right]
#             # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
#             right = mid
#     # loop ends when left = right
#     return left
#
#
# print(search_smallest(list4))




# # 6. compute the integer square root
#
# def square_root(k):
#     # Candidate interval [left, right] where everything before left has square
#     # smaller than k, everything right has square greater than k.
#     left, right = 0, k
#     while left <= right:
#         mid = (left + right) // 2
#         mid_squared = mid * mid
#         if mid_squared <= k:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left - 1
#
# print(square_root(101))




# # 7. compte the real square root
#
# def real_square_root(x):
#     # Decides the search range according to x's value relative to 1.0.
#     left, right = (x, 1.0) if x < 1.0 else (1.0, x)
#
#     # Keeps searching as long as left != right.
#     while not math.isclose(left, right):
#         mid = 0.5 * (left + right)
#         mid_squared = mid * mid
#         if mid_squared > x:
#             right = mid
#         else:
#             left = mid
#
#     return left
#
# print(real_square_root(2.51))




# # 8. search in a 2D sorted array
#
# A = [[-1, 2, 4, 4, 6],
#      [1, 5, 5, 9, 21],
#      [3, 6, 6, 9, 22],
#      [3, 6, 8, 10, 24],
#      [6, 8, 9, 12, 25],
#      [8, 10, 12, 13, 40]]
#
# def matrix_search(A, x):
#     row, col = 0, len(A[0]) - 1 # start from the top-right corner.
#
#     # keeps searching while there are unclassified rows and columns.
#     while row < len(A) and col >= 0:
#         if A[row][col] == x:
#             return True
#         elif A[row][col] < x:
#             row += 1  # eliminate this row.
#         else:  # A[row][col] > x
#             col -= 1  # eliminate this column.
#
#     return False
#
# print(matrix_search(A, 10))




# # 9. find the min and the max simutaneously
#
# list5 = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
#
# MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
#
# def find_min_max(A):
#     def min_max(a, b):
#         return MinMax(a, b) if a < b else MinMax(b, a)
#
#     if len(A) <= 1:
#         return MinMax(A[0], A[0])
#
#     global_min_max = min_max(A[0], A[1])
#
#     # process two elements at a time
#     for i in range(2, len(A) - 1, 2):
#         local_min_max = min_max(A[i], A[i + 1])
#         global_min_max = MinMax(min(global_min_max.smallest, local_min_max.smallest), max(global_min_max.largest, local_min_max.largest))
#
#
#     # if there is odd number of elements in the array, we still need to
#     # compare the last element with the existing answer.
#     if len(A) % 2:
#         global_min_max = MinMax(min(global_min_max.smallest, A[-1]), max(global_min_max.largest, A[-1]))
#
#     return global_min_max
#
# print(find_min_max(list5))




# 10. find kth largest

list6 = [3, 1, -1, 2]

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

        raise IndexError('no k-th node in array A')

    return find_kth(operator.gt)

print(find_kth_largest(1, list6))





















