from typing import Optional


def bin_search(sorted_array: list[int], looking_for: int) -> Optional[int]:
    """
    Binary search realization, that find the position of the searched element, otherwise return None
    Time Complexity is O(log n)
    Space Complexity is O(1)"""
    left_side, right_side = 0, len(sorted_array) - 1
    while left_side <= right_side:
        middle = (left_side + right_side) // 2
        if looking_for > sorted_array[middle]:
            left_side = middle + 1
        elif looking_for < sorted_array[middle]:
            right_side = middle - 1
        else:
            return middle + 1
    return


def main():
    assert bin_search([1, 2, 3], 3) == 3
    assert bin_search([1, 2, 3], 156) is None
    assert bin_search([], 156) is None
    assert bin_search([1, 341, 111, 31], 1) == 1


if __name__ == '__main__':
    main()
