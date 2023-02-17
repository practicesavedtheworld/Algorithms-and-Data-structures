import os
import random
import re
import sys
import unittest

sys.path.append(os.path.join(sys.path[0], '..'))
from bubble_sort import bubble_sorted
from find_all_modules import get_all_modules
from quick_sort import quick_sorted
from selection_sort import selection_sorted
from Exceptions_.exceptions_sorting import WrongInnerTypeOfArray


class TestBubbleSortRealization(unittest.TestCase):

    @staticmethod
    def __modules():
        current_modules = get_all_modules(f'{__name__}.py')
        sorting_modules = [f"{md}ed" for md in current_modules if re.fullmatch(r'.*sort.*', md)]
        return sorting_modules

    def test_empty_arrays(self):
        modules = self.__modules()
        error_message = 'Wrong result. It should be empty result'
        for md in modules:
            self.assertEqual(eval(f'{md}([])'), [], error_message)

    def test_array_of_integers_sorting(self):
        modules = self.__modules()
        error_message = 'Wrong result of sorting. It should sort like this [4, -2, 4, 0] => [-2, 0, 4, 4]'
        for _ in range(50):
            random_array = [random.randint(i, i ** 2) for i in range(-500, 500)]
            for md in modules:
                self.assertEqual(eval(f"{md}(random_array)"), sorted(random_array), error_message)

    def test_exceptions(self):
        modules = self.__modules()
        for md in modules:
            self.assertRaises(WrongInnerTypeOfArray, eval(md), ['1,', 1, -3])


if __name__ == '__main__':
    unittest.main()
