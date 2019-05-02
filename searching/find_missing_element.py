
import bisect, collections, math, operator, random, itertools


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




# # 10. find kth largest
#
# list6 = [3, 1, -1, 2]
#
# # The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# # find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# # find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
# def find_kth_largest(k, A):
#     def find_kth(comp):
#         # Partition A[left:right + 1] around pivot_idx, returns the new index of
#         # the pivot, new_pivot_idx, after partition. After partitioning,
#         # A[left:new_pivot_idx] contains elements that are "greater than" the
#         # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
#         # "less than" the pivot.
#         #
#         # Note: "greater than" and "less than" are defined by the comp object.
#         #
#         # Returns the new index of the pivot element after partition.
#         def partition_around_pivot(left, right, pivot_idx):
#             pivot_value = A[pivot_idx]
#             new_pivot_idx = left
#             A[pivot_idx], A[right] = A[right], A[pivot_idx]
#             for i in range(left, right):
#                 if comp(A[i], pivot_value):
#                     A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
#                     new_pivot_idx += 1
#             A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
#             return new_pivot_idx
#
#         left, right = 0, len(A) - 1
#         while left <= right:
#             # Generates a random integer in [left, right].
#             pivot_idx = random.randint(left, right)
#             new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
#             if new_pivot_idx == k - 1:
#                 return A[new_pivot_idx]
#             elif new_pivot_idx > k - 1:
#                 right = new_pivot_idx - 1
#             else:  # new_pivot_idx < k - 1.
#                 left = new_pivot_idx + 1
#
#         raise IndexError('no k-th node in array A')
#
#     return find_kth(operator.gt)
#
# print(find_kth_largest(1, list6))




# 11. Find the missing IP address

list7 = [766, 992, 49, 258, 377, 539, 496, 114, 757, 284, 26, 928, 470, 327, 953, 383, 559, 516, 444, 537, 805, 795, 503, 277, 399, 664, 314, 533, 50, 359, 848, 959, 692, 222, 509, 806, 335, 920, 568, 631, 409, 188, 339, 221, 628, 262, 868, 522, 882, 31, 580, 927, 989, 468, 866, 141, 646, 358, 843, 313, 5, 557, 133, 797, 536, 281, 332, 226, 800, 564, 553, 538, 840, 90, 83, 973, 775, 390, 428, 433, 870, 488, 880, 413, 951, 143, 357, 711, 744, 256, 903, 672, 172, 44, 395, 983, 543, 492, 81, 847, 809, 46, 278, 144, 407, 591, 323, 727, 519, 620, 311, 29, 962, 128, 586, 57, 876, 563, 743, 767, 378, 836, 101, 289, 943, 774, 436, 493, 38, 266, 27, 224, 911, 624, 610, 11, 812, 912, 677, 126, 419, 10, 67, 177, 309, 615, 644, 14, 98, 481, 394, 100, 452, 307, 601, 269, 818, 202, 229, 87, 125, 913, 640, 764, 904, 276, 941, 45, 230, 259, 477, 111, 980, 704, 148, 167, 647, 883, 349, 54, 799, 373, 755, 302, 823, 865, 275, 356, 554, 124, 213, 82, 446, 86, 152, 669, 511, 25, 296, 996, 507, 541, 605, 329, 59, 594, 660, 715, 782, 39, 831, 255, 822, 423, 721, 976, 448, 130, 978, 643, 910, 949, 252, 633, 708, 64, 938, 572, 603, 247, 474, 139, 773, 306, 807, 612, 174, 238, 523, 668, 997, 855, 821, 466, 987, 21, 153, 681, 422, 587, 495, 145, 435, 283, 935, 118, 702, 802, 579, 2, 136, 635, 532, 33, 598, 80, 680, 0, 364, 376, 418, 734, 180, 482, 360, 986, 69, 107, 316, 739, 386, 737, 321, 897, 415, 424, 670, 616, 121, 944, 99, 408, 305, 899, 719, 663, 588, 417, 85, 732, 606, 41, 780, 154, 47, 199, 798, 389, 864, 898, 37, 225, 236, 264, 447, 194, 926, 463, 726, 637, 35, 439, 974, 165, 909, 385, 700, 629, 254, 597, 674, 20, 788, 365, 426, 869, 250, 642, 576, 895, 966, 384, 829, 380, 600, 828, 515, 137, 301, 661, 251, 729, 746, 534, 725, 838, 505, 317, 954, 527, 923, 190, 312, 801, 184, 830, 796, 379, 735, 161, 195, 979, 545, 765, 334, 353, 689, 93, 756, 43, 971, 240, 759, 176, 592, 619, 556, 104, 862, 324, 745, 632, 484, 550, 714, 900, 694, 182, 328, 888, 375, 885, 622, 464, 330, 772, 636, 453, 320, 142, 784, 52, 7, 22, 955, 214, 63, 441, 571, 105, 968, 208, 975, 102, 169, 544, 891, 61, 451, 479, 929, 832, 120, 149, 1, 206, 947, 487, 561, 582, 504, 243, 68, 617, 762, 123, 540, 387, 400, 952, 84, 220, 32, 916, 826, 525, 945, 751, 116, 988, 363, 92, 969, 412, 122, 303, 933, 758, 501, 666, 450, 457, 76, 483, 815, 750, 300, 713, 465, 70, 404, 878, 776, 921, 462, 608, 528, 837, 458, 239, 140, 162, 850, 998, 535, 595, 703, 956, 159, 431, 752, 326, 227, 712, 526, 961, 699, 932, 549, 599, 849, 23, 147, 216, 210, 398, 113, 267, 573, 185, 924, 270, 288, 78, 430, 355, 310, 106, 804, 860, 707, 871, 985, 192, 803, 371, 497, 212, 741, 948, 627, 813, 331, 506, 675, 119, 73, 205, 844, 109, 319, 79, 662, 827, 738, 151, 618, 575, 346, 793, 235, 134, 459, 811, 833, 678, 667, 574, 112, 402, 902, 425, 653, 367, 857, 234, 810, 555, 520, 698, 676, 272, 461, 325, 204, 548, 879, 957, 886, 53, 478, 350, 701, 286, 889, 845, 940, 761, 232, 60, 614, 649, 656, 577, 343, 24, 786, 146, 982, 336, 427, 613, 965, 218, 936, 905, 705, 420, 3, 183, 396, 115, 273, 589, 623, 445, 129, 449, 970, 429, 567, 931, 186, 97, 688, 245, 546, 274, 749, 471, 193, 157, 967, 62, 342, 348, 881, 333, 287, 894, 872, 569, 17, 560, 244, 372, 370, 919, 201, 257, 48, 513, 178, 341, 651, 368, 659, 285, 456, 351, 88, 207, 476, 34, 717, 696, 963, 873, 730, 960, 292, 771, 835, 401, 665, 369, 253, 679, 8, 578, 500, 405, 51, 66, 490, 297, 414, 685, 131, 596, 742, 884, 110, 652, 547, 785, 280, 846, 103, 856, 215, 36, 411, 790, 231, 999, 791, 485, 641, 887, 763, 842, 4, 472, 228, 16, 918, 858, 964, 219, 345, 156, 529, 820, 723, 825, 40, 720, 72, 604, 930, 814, 994, 237, 521, 473, 769, 163, 388, 438, 877, 695, 318, 908, 524, 241, 298, 393, 74, 593, 443, 340, 217, 397, 655, 13, 824, 565, 460, 246, 117, 261, 779, 728, 901, 914, 191, 562, 863, 242, 570, 494, 347, 18, 621, 733, 89, 602, 166, 30, 934, 747, 673, 179, 650, 709, 290, 454, 639, 991, 155, 223, 984, 168, 581, 645, 542, 42, 658, 792, 248, 132, 135, 841, 28, 874, 753, 374, 260, 77, 382, 770, 958, 626, 706, 638, 777, 282, 789, 950, 687, 410, 138, 819, 170, 731, 291, 915, 203, 906, 233, 875, 187, 896, 200, 890, 94, 760, 467, 512, 946, 6, 489, 816, 514, 566, 9, 861, 15, 486, 56, 718, 127, 434, 299, 817, 892, 175, 392, 150, 942, 75, 683, 158, 607, 583, 338, 508, 265, 502, 354, 437, 198, 530, 173, 625, 196, 209, 95, 859, 403, 362, 977, 263, 609, 654, 518, 315, 164, 585, 249, 189, 391, 271, 768, 671, 634, 65, 455, 748, 337, 710, 851, 907, 778, 71, 682, 58, 993, 344, 839, 939, 893, 366, 55, 697, 611, 853, 352, 584, 781, 852, 981, 475, 416, 469, 406, 716, 294, 268, 211, 510, 691, 308, 96, 361, 787, 917, 442, 108, 794, 925, 808, 736, 990, 498, 171, 440, 686, 693, 531, 91, 922, 197, 590, 740, 304, 972, 322, 834, 722, 295, 551, 867, 480, 381, 783, 181, 499, 754, 690, 517, 684, 12, 421]



def find_missing_element(stream):

    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)



    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # look for a bucket that contains less than (1 << 16) elements.
    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)

    # finds all ip addresses in the stream whose first 16 bits are equal to candidate_bucket.
    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy

    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # records the presence of 16 LSB of x.
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1


    # at least one of the LSB combinations is absent, find it.
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i



print(find_missing_element(list7))



































