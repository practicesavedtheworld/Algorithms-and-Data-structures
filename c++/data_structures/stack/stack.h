#include <cstdint>

namespace CustomStack {
/*
Data structure that store elements in an array. It works
like a stack in a LIFO order. So, it lets us push and pop elements.
Pop and push are O(1) operations.
*/
class ArrayBasedStack
{
public:
    uint64_t limit;
    int top;
    int64_t * storage = nullptr;

    explicit ArrayBasedStack(uint64_t limit);

    void push(int64_t element);

    int64_t pop();
};
} // namespace CustomStack