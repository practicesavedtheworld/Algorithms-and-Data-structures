#include <iostream>

namespace RadixSort
{
    // Receives number of bits in a number
    // Working case: getBitCount(255) = 8 (11111111)
    u_int8_t getBitCount(u_int64_t number);

    /* Radix sort idea is to sort the elements based on their bit values.
    I will use 2 groups for 0 and 1 bit values. Then compare every radix
    group with the 1/0 bit. Next step will be to update base array with
    group values. It'll be like: [el, el, el, el, el, el, el, el] => [0, 0, 0, 1, 1, 1, 1, 1]
    0 and 1 means element in 0 or 1 groups.
    It continues until I don't pass through last radix.
    Working result: [2, 100, 1, 783, 4, 31, 0, -34] => [-34, 0, 1, 2, 4, 31, 100, 783]
    */
    void radixSort(int16_t arr[], size_t arr_size, int16_t max_element);
} // namespace RadixSort
