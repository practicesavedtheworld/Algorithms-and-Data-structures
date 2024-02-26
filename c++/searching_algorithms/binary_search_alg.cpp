#include <iostream>
#include "binary_search_alg.h"

#define NO_ELEMENT_FOUND (-1)

// Finds desired element index. If no element was found returns -1.
// Since there is no chance to get the array length from pointer we need to pass it as parameter.
// It works only with sorted arrays.
int64_t binary_search2(const int64_t* sorted_arr, const int64_t sorted_arr_length, int64_t looking_for)
{
    // [0, 1, 2, 3, 4]  - 4
    int64_t left_side = 0;
    auto right_side = sorted_arr_length;
    // Time complexity - O(log(n))
    // Space complexity - O(1)
    while (left_side < right_side)
    {
        auto middle = (right_side + left_side) / 2;
        auto current_element = sorted_arr[middle];

        if (current_element == looking_for) return middle;
        else if (current_element > looking_for) right_side = middle - 1;
        else left_side = middle + 1;
    }
    return  NO_ELEMENT_FOUND;
}
