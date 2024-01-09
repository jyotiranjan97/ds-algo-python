from typing import List


def binary_search(arr: List[int], target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search([2, 4, 5, 6, 8, 10, 23, 25], 6))
print(binary_search([2, 4, 5, 6, 8, 10, 23, 25], 7))
