from python.validators.sorting_validator import validate_array_of_numbers


@validate_array_of_numbers(parameter='list')
def bubble_sort_in_place(arr: list[int]) -> None:
    """
    Sorting array in place. Does not create new object.
    Time complexity is O(n^2)
    Space complexity is O(1)
    :param arr:list[int]
    :return: None
    """
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@validate_array_of_numbers(parameter='list')
def bubble_sorted(arr: list[int]) -> list[int]:
    """
    Create a copy of the given array, sorting it. Does not sort the origin array. It returns sorted copy.
    Time complexity is O(n^2)
    Space complexity is O(n)
    :param arr:list[int]
    :return: list[int]
    """
    arr_copy = arr.copy()
    bubble_sort_in_place(arr_copy)
    return arr_copy


def main():
    """Testing our sorting
    Assume that we received correct type(list[int])
    """
    assert bubble_sorted([1, -2, -4, 2, 10, 0, -19]) == [-19, -4, -2, 0, 1, 2, 10]
    assert bubble_sorted([1]) == [1]
    assert bubble_sorted([]) == []
    assert bubble_sorted([2, 3, -33]) == [-33, 2, 3]


if __name__ == "__main__":
    main()
