#include <iostream>
#include <vector>

namespace QuickSort {
/*
 * This quick sort realization is based on the idea of divide and conquer.
 * It returns new sorted vector.
 * Firstly we need to chose 'good' pivot element, so we do it randomly.
 * I separate the array into three parts: <pivot, =pivot, >pivot.
 * Elements that in the =pivot part are already sorted, so we need recursively
 * sort other two parts.
 *
 * quickSort([3, 1, 4, 2])
             |
             v
          pivot = 3
      /       |        \
    [1, 2]   [3]        [4]
 *
 * Time complexity: O(n * log(n))
 * Space complexity: O(n) - returns new vector
 */
std::vector<int64_t> quickSort(std::vector<int64_t> &arr);
}