#include "radix_sort.h"
#include <vector>


namespace RadixSort {

    u_int8_t getBitCount(u_int64_t number)
    {
        u_int8_t bit_count = 0;
        while (number > 0) {
            number >>= 1;
            bit_count++;
        }
        return bit_count;
    }

    void radixSort(int16_t arr[], size_t arr_size, int16_t max_element)
    {

        // Time complexity: O(N * log(MaxElement))
        // Space complexity: O(N)
        u_int8_t bit_count = getBitCount(max_element);
        for (int radix = 0; radix < bit_count; radix++) {
            // Converting decimal to binary and push it into the corresponding group, which is either zero or one.
            auto zero_bits_group = new std::vector<int16_t>();
            auto one_bits_group = new std::vector<int16_t>();
            // Depending on the first bit of the number, push it into different group.
            for (int i = 0; i < arr_size; i++)
            {
                if (((arr[i] >> radix) & 1) == 1)
                {
                    one_bits_group->push_back(arr[i]);
                }
                else zero_bits_group->push_back(arr[i]);
            }

            // Updating the array with the sorted numbers based on radix.
            auto idx = 0;
            for (auto z_bit: *zero_bits_group) arr[idx++] = z_bit;
            for (auto o_bit: *one_bits_group) arr[idx++] = o_bit;

            delete zero_bits_group;
            delete one_bits_group;
        }
    }
} // namespace RadixSort