#include "fast_power.h"

namespace FastPower {
int64_t fast_power(int number, int power)
{
    if (power == 0) return 1;
    if (power == 1) return number;

    // Time complexity: O(log(n). Worst case: O(n)
    // Space complexity: O(1)
    int64_t sub_result = fast_power(number, power / 2);
    if (power % 2 == 0)
        return sub_result * sub_result;
    return sub_result * sub_result * number;
}
} // namespace FastPower