from typing import List

# An array of boolean values is divided into two sections;
# the left section consists of all false and the right section consists of all true.
# Find the First True in a Sorted Boolean Array of the right section, i.e. the index of the first true element.
# If there is no true element, return -1.
#
# Input: arr = [false, false, true, true, true]
#
# Output: 2


# Brute Froce
def find_first_true_brute(arr: List[bool]) -> int:
    for key, val in enumerate(arr):
        if val:
            return key

    return -1


def find_first_true(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_idx


print(find_first_true_brute([False, False, True, True, True]))
print(find_first_true([False, False, True, True, True]))
