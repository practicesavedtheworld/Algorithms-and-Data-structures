#include "merge_sort.h"

namespace MergeSort {
void merge(double arr[], u_int left, u_int middle, u_int right)
{
    // 17. case 1 to 17. middle = (1+17) / 2 = 9.
    // first -> 9 - 1 + 1 = 9
    // second -> 17 - 9 = 8
    // assert 9+8 == 17
    u_int sub_first_arr_len = middle - left + 1;
    u_int sub_second_arr_len = right - middle;

    // Temp arrays
    auto *left_sub_array = new double[sub_first_arr_len];
    auto *right_sub_array = new double[sub_second_arr_len];

    // Copying values from original array
    for (int i = 0; i < sub_first_arr_len; i++)
        left_sub_array[i] = arr[left + i];
    for (int j = 0; j < sub_second_arr_len; j++)
        right_sub_array[j] = arr[middle + 1 + j];

    u_int   left_sub_array_idx = 0,
            right_sub_array_idx = 0,
            original_array_idx = left;

    while (left_sub_array_idx < sub_first_arr_len
           &&
           right_sub_array_idx < sub_second_arr_len)
    {
        if (left_sub_array[left_sub_array_idx] <= right_sub_array[right_sub_array_idx])
            arr[original_array_idx++] = left_sub_array[left_sub_array_idx++];
        else
            arr[original_array_idx++] = right_sub_array[right_sub_array_idx++];
    }

    // Push remaining elements, that 100% already sorted
    while (left_sub_array_idx < sub_first_arr_len)
        arr[original_array_idx++] = left_sub_array[left_sub_array_idx++];
    while (right_sub_array_idx < sub_second_arr_len)
        arr[original_array_idx++] = right_sub_array[right_sub_array_idx++];

    delete []left_sub_array;
    delete []right_sub_array;
}
void mergeSort(double arr[], u_int begin_index, u_int end_index)
{
    if (end_index > MAX_ARRAY_SIZE)
    {
        throw std::out_of_range("Array size is too big");
    }
    if (begin_index >= end_index) return;

    u_int middle = begin_index + (end_index - begin_index) / 2;
    mergeSort(arr, begin_index, middle);
    mergeSort(arr, middle + 1, end_index);

    merge(arr, begin_index, middle, end_index);

}
} // namespace MergeSort