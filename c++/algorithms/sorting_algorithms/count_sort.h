#include <cstdint>
#include <cstdio>


namespace CountSort
{
    /*
      Count Sort
      Passes through the array and add each element to map.
      Key: Element
      Value: Count
      Since map based on red black tree, we can use it to sort
      the array by keys in log(n) time.
      Final step is change the original array by passing through
      the map

      Working case: [10, 2, 0, -88, 4] -> [-88, 0, 2, 4, 10]
     */
    void countSort(int64_t *arr, size_t arr_size);
} // namespace CountSort