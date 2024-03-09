#include <iostream>
#include <vector>


// Creates mask for receiving prime numbers in range.
// Mask contain 0 or 1 values. 1 means that number is prime.
// Upper limit not included.
std::vector<u_int64_t> primes(u_int64_t limit)
{
    /*
    --------------------
     2, 3, 4, 5, 6,
     7, 8, 9, 10, 11,
     12, 13, 14, 15, 16,
     17, 18, 19, 20, 21,
     22, 23, 24, 25, 26,
    --------------------
    */
    if (limit < 3)
    {
        std::cerr << "There are no prime numbers in range. Limit(range) must be > 3" << std::endl;
        return {};
    }
    /*
                             Eratosthenes sieve idea
    */
    // Prime X number means that every X*X*(1...inf) number definitely will be composite.
    // First prime number always equal 2. By default, mask has all numbers as prime,
    // so after first iteration we exclude all numbers that (X%2==0) and have > 2 dividers
    // After iteration with 7, this algorithm found sqrt(limit), so its almost 1/2 of
    // all prime numbers in range (1...limit)

    // Time complexity O(n*log(log n)). Best case O(n)
    // Space complexity O(n)
    std::vector<bool> prime_mask(limit, true);
    for (auto j = 2; j < limit; j++)
    {
        if (prime_mask[j])
        {
            for (auto k = j + j; k < limit; k+=j) prime_mask[k] = false;
        }
    }

    // Fill vector with prime numbers
    std::vector<u_int64_t> primes_list;
    for (auto idx = 2; idx < limit; idx++)
    {
        if (prime_mask[idx]) primes_list.push_back(idx);
    }

    return primes_list;
}

void print_primes(const std::vector<u_int64_t>& primes_list)
{
    for (auto prime : primes_list) std::cout << prime << " ";
    std::cout << std::endl;
}