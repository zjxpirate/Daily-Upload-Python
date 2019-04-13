
import bisect, collections


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




# 6. compute the integer square root

def square_root(k):
    # Candidate interval [left, right] where everything before left has square
    # smaller than k, everything right has square greater than k.
    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

print(square_root(101))










