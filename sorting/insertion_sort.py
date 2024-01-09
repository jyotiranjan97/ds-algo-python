from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    for idx, entry in enumerate(unsorted_list):
        current = idx
        while current > 0 and unsorted_list[current] > unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1

    return unsorted_list


print(sort_list([3, 5, 1, 10, 4, 9, 8]))
print(sort_list([3]))
