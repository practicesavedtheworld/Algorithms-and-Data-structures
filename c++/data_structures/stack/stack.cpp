#include <iostream>

#include "stack.h"

namespace CustomStack
{
    ArrayBasedStack::ArrayBasedStack(uint64_t limit)
    {
        this->limit = limit;
        this->top = -1;
        this->storage = new int64_t[limit];
    }

    int64_t ArrayBasedStack::pop()
    {
        if (this->top < 0)
        {
            std::cerr << "Stack is empty";
            return -1;  // Default value if stack empty
        }

        return this->storage[this->top--];
    }

    void ArrayBasedStack::push(int64_t element)
    {
        if (this->top == this->limit -1)
        {
            std::cerr << "Stack is full. Cannot add element";
            return;
        }
        this->storage[++(this->top)] = element;
    }
}  // namespace CustomStack