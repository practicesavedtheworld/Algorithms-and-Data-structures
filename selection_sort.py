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


def selection_sorted(arr: tuple[int, ...] | list[int]) -> list[int]:
    """

    :param arr:
    :return:
    """
    pass

def main():
    """Testing our sorting"""
    pass


if __name__ == '__main__':
    main()
