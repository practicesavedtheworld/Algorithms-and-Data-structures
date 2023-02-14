from Validators_.sorting_validator import validate_array_of_integers


@validate_array_of_integers(parameter='list')
def selection_sort_in_place(arr: list[int]) -> None:
    """
    Do sort stuff to the given array. The sorting performed in place, so it does not return new array, it returns None
    [1, 0, -2, -42, 3] => [-42, -2, 0, 1, 3]
    Time complexity is O(n*n) => O(n^2)
    Space complexity is O(1)
    :param arr: list[int]
    :return: None
    """
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]


@validate_array_of_integers(parameter='list')
def selection_sorted(arr: list[int]) -> list[int]:
    """
    Create copy of the given array and sorting it. Does not change the original array, return new sorted object.
    Time complexity is O(n^2), n == len(arr)
    Space complexity is O(n)
    :param arr: list[int]
    :return: list[int]
    """
    arr_copy = arr.copy()
    selection_sort_in_place(arr_copy)
    return arr_copy


def main():
    """Testing our sorting"""
    assert selection_sorted([-2, 3, -2, -111, 0, 22]) == [-111, -2, -2, 0, 3, 22]
    assert selection_sorted([-2, 3]) == [-2, 3]
    assert selection_sorted([3]) == [3]
    assert selection_sorted([0, -2, 3]) == [-2, 0, 3]


if __name__ == '__main__':
    main()
