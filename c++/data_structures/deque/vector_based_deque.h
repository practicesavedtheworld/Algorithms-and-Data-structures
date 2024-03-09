#include <vector>


// Implementation of deque using vector.
// Educational purposes.
class VectorBasedDeque {
public:
    explicit VectorBasedDeque(int capacity) : deq(capacity, 0), front_index(0), back_index(0) {};

    void pushFront(int value);
    void pushBack(int value);

    int popFront();
    int popBack();

    bool isFull();
    void increaseDequeCapacity();

    void showAll();

private:
    size_t front_index;
    size_t back_index;
    std::vector<int> deq;
};
