#include "selection_sort.h"


namespace SelectionSort {
void selectionSort(int64_t arr[], size_t arr_size)
{

    // Time complexity: O(N^2). Worst case: O(N^2)
    // Space complexity: O(1)
    for (int pos = 0; pos < arr_size - 1; pos++)
    {
        int min = pos;
        for (int i = pos + 1; i < arr_size; i++)
        {
            if (arr[i] < arr[min]) min = i;
        }
        int64_t tmp = arr[pos];
        arr[pos] = arr[min];
        arr[min] = tmp;
    }
}
} // namespace SelectionSort