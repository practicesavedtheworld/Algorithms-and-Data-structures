#include <cstdint>

namespace FastPower
{
    /* Fast power algorithm
     * The idea is to use binary exponentiation to compute the power of a number.
     * Invariant: number^1 = number
     *            number^0 = 1
     * Instead of using multiplication, we use power multiplication.
     * number^20 = number^10 * number^10
     * number^10 = number^5 * number^5
     */
    int64_t fast_power(int number, int power);
} // namespace FastPower