#include "insertion_sort.h"

// Sorting in place, changes array, returns nothing.
void insertionSort(int array[], int array_size)
{
    if (array_size < 2) return;

    // The idea of insertion sort is to compare each element with the previous ones.
    // If the elements is lower than previous element, swap them. It continues until
    // element is not lower than previous one, or it has been placed at the beginning.
    // Working example: [5, 3, 2, 4, 1] -> [1, 2, 3, 4, 5]

    // Time complexity O(n^2). Best case O(n).
    // Space complexity O(1).
    for (int i = 1; i < array_size; i++)
    {
        int current_element = array[i];
        int previous = i - 1;
        while (previous >= 0 && array[previous] > current_element)
        {
            array[previous + 1] = array[previous];
            previous--;
        }
        array[previous + 1] = current_element;
    }

}