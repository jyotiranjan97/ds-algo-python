from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    length = len(unsorted_list)

    if length <= 1:
        return unsorted_list

    mid = length // 2
    left_list, right_list = sort_list(unsorted_list[:mid]), sort_list(unsorted_list[mid:])

    result_list = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < mid or right_pointer < length - mid:
        if left_pointer == mid:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == length - mid:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list


print(sort_list([3, 5, 1, 10, 4, 9, 8]))
print(sort_list([3]))
