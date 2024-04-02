#include <cstdlib>     /* srand, rand */
#include <ctime>       /* time */

#include "quick_sort.h"

using std::vector;
namespace QuickSort {

vector<int64_t> quickSort(vector<int64_t> &arr)
{
    if (arr.size() <= 1) return arr;

    srand(time(nullptr));
    auto pivot = rand() % (arr.size() - 1);

    // Arrays for lesser, equal and greater elements
    vector<int64_t> lesser_elements, equal_elements, greater_elements;

    for (int i = 0; i < arr.size(); ++i)
    {
        if (arr[i] > arr[pivot])
            greater_elements.push_back(arr[i]);
        else if(arr[i] == arr[pivot])
            equal_elements.push_back(arr[i]);
        else
            lesser_elements.push_back(arr[i]);
    }
    // Sort lesser and greater elements
    lesser_elements = quickSort(lesser_elements);
    greater_elements = quickSort(greater_elements);

    vector<int64_t> final_vector;
    final_vector.insert(final_vector.end(), lesser_elements.begin(), lesser_elements.end());
    final_vector.insert(final_vector.end(), equal_elements.begin(), equal_elements.end());
    final_vector.insert(final_vector.end(), greater_elements.begin(), greater_elements.end());

    return final_vector;
}
} // namespace QuickSort