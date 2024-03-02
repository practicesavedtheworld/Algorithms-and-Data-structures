#include "bubble_sort.h"

// Sorts an array in place, changes the array, returns nothing
void bubbleSort(int64_t array[], int array_size)
{
    if (array_size < 2) return;


    // The bubble sort idea is to swap nearest neighbors if they are in wrong order.
    // Move the biggest number to the end of the array.
    // Working case:
    // [3, 10, 2, 0, 103, 44, 1] -> [0, 1, 2, 3, 10, 44, 103]

    // Time complexity: O(n^2). Best case: O(n).
    // Space complexity: O(1).
    for (int i = 0; i < array_size - 1; i++)
        for (int j = 0; j < array_size - i - 1; j++)
        {
            if (array[j] > array[j+1])
            {
                int64_t tmp = array[j];
                array[j] = array[j+1];
                array[j + 1] = tmp;
            }
        }
}