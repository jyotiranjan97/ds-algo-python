from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    length = len(unsorted_list)

    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if unsorted_list[j] < unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break

    return unsorted_list


print(sort_list([3, 5, 1, 10, 4, 9, 8]))
print(sort_list([3]))
