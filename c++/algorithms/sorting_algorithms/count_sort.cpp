#include "count_sort.h"
#include <map>


namespace CountSort {
// Using ordered map
void countSort(int64_t *arr, size_t arr_size)
{
    //  Time complexity: O(n)
    //  Space complexity: O(n)
    std::map<int64_t, int64_t> number_counter;
    for (int i = 0; i < arr_size; i++)
    {
        auto current_element = arr[i];
        if (number_counter.find(current_element) != number_counter.end())
        {
            number_counter[current_element]++;
        }
        else number_counter[current_element] = 1;
    }

    int idx = 0;
    for (auto &pair: number_counter)
        for (int i = 0; i < pair.second; i++)
        {
            arr[idx++] = pair.first;
        }

}
} // namespace CountSort