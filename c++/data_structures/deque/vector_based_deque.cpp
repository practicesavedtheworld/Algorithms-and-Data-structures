#include <iostream>
#include "vector_based_deque.h"


void VectorBasedDeque::pushFront(int value) {
    if (isFull()) increaseDequeCapacity();
    // O(n)
    for (auto i = this->back_index; i > this->front_index; --i) {
        this->deq[i] = this->deq[i - 1];
    }

    this->deq[this->front_index] = value;
    this->back_index += 1;
}


void VectorBasedDeque::pushBack(int value) {
    if (isFull()) increaseDequeCapacity();

    this->deq[back_index] = value;
    this->back_index += 1;
}


int VectorBasedDeque::popFront() {
    // So this is O(n) because of shifting
    int removed_value = this->deq[front_index];
    for (int i = 0; i < this->deq.size() - 1; i++) {
        this->deq[i] = this->deq[i + 1];
    }

    std::cout << "popFront" << removed_value << std::endl;
    return removed_value;
}


int VectorBasedDeque::popBack() {
    if (this->back_index == 0) {
        std::cerr << "Deque is empty!" << std::endl;
        return -1;
    }

    this->back_index -= 1;
    int removed_value = this->deq[this->back_index];
    this->deq[this->back_index] = 0;

    return removed_value;
}


bool VectorBasedDeque::isFull() {
    size_t cap = this->deq.capacity();
    return this->deq.size() == cap && this->deq[cap - 1] != 0;
}

// O(n)
// Creates new vector with double capacity and copies all elements
void VectorBasedDeque::increaseDequeCapacity() {
    std::vector<int> bigger_deq(this->deq.capacity() * 2);
    for (int i = 0; i < this->deq.size(); i++) {
        bigger_deq[i] = this->deq[i];
    }
    this->deq = bigger_deq;

}

void VectorBasedDeque::showAll() {
    for (int i = 0; i < this->deq.size(); i++) {
        if (this->deq[i] == 0) break;
        std::cout << this->deq[i] << std::endl;
    }

}
