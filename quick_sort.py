import random
from Validators_.sorting_validator import validate_array_of_numbers


@validate_array_of_numbers(parameter='list')
def quick_sorted(array_: list[int], classic: bool = True) -> list[int]:
    """
    Quick sort algorithm that doesn't sort original array, it creates new object based sort it and return.
    Time complexity is based on pivot. In classic realization pivot every time is a random element.
                                       So at most it'll be O(n log n), worst case O(n^2)
    Space complexity is O(n), sometimes its O(log n)
    :param array_: list[int]
    :param classic: bool
    :return: list[int]
    """
    if len(array_) < 2:
        return array_
    current_index = random.randint(0, len(array_) - 1) if classic else 0
    pivot = array_[current_index]
    left_side = [number for number in array_[:current_index] + array_[current_index + 1:] if number <= pivot]
    right_side = [number for number in array_[:current_index] + array_[current_index + 1:] if number > pivot]
    return quick_sorted(left_side) + [pivot] + quick_sorted(right_side)


def main():
    print(quick_sorted([2, 1, 0, -33, 20, 423, -221, 0]))
    assert quick_sorted([2, 1, 0]) == [0, 1, 2]


if __name__ == '__main__':
    main()