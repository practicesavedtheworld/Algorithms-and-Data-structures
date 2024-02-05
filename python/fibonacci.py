from functools import lru_cache
from typing import Generator


@lru_cache
def fib_dynamic(number: int) -> int:
    """

    :param number: int
    :return: int
    """
    current_fib_number, next_fib_number = 0, 1
    for _ in range(2, number + 1):
        current_fib_number, next_fib_number = next_fib_number, current_fib_number + next_fib_number
    return current_fib_number


@lru_cache
def fib_dynamic_list(number: int) -> list[int]:
    """

    :param number: int
    :return: list[int]
    """
    all_fib_numbers = [0] * number
    all_fib_numbers[0], all_fib_numbers[1] = 0, 1
    for i in range(2, number):
        all_fib_numbers[i] = all_fib_numbers[i - 1] + all_fib_numbers[i - 2]
    return all_fib_numbers


def fib_iterator() -> Generator[int]:
    pass


def main():
    pass


if __name__ == '__main__':
    pass
