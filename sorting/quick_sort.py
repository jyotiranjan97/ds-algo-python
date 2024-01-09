from typing import List


def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    while start_ptr < end_ptr:
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)


def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list


print(sort_list([3, 5, 1, 10, 4, 9, 8]))
print(sort_list([3]))
