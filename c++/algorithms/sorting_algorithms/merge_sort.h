#include <iostream>

const int MAX_ARRAY_SIZE = 100000;

namespace MergeSort {
/*
 * Merge Sort idea is to divide the array into smaller subarrays
 * and then merge them together in sorted order.
 * Dividing example
 *              [2, 4, 1, -19, 0, 93, 3]
                  /              \
         [2, 4, 1, -19]        [0, 93, 3]
          /       \              /      \
    [2, 4]     [1, -19]      [0, 93]    [3]
    /   \        /    \        /   \
  [2]   [4]   [1]   [-19]   [0]   [93]
  Time Complexity: O(n * log(n))
  Space Complexity: this realization is O(n)
 */
void mergeSort(double arr[], u_int begin_index, u_int end_index);

/*
 * Merging example
 *               [2, 4, 1, -19, 0, 93, 3]
                 /               \
         [1, 2, 4, -19]         [0, 3, 93]
               /                       \
       [-19, 1, 2, 4]             [0, 3, 93]
                     \                   /
                    [-19, 0, 1, 2, 3, 4, 93]
 */
void merge(double arr, u_int begin_index, u_int middle, u_int end_index);
} // namespace MergeSort