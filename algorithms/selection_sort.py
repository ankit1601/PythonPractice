"""
In work on the mechanism of swapping smallest value with current element
This way we will swap first element with smallest in the list and so on
"""


def selection_sort(arr):
    print("length", len(arr))
    count = 0
    for i in range(0, len(arr)):
        print(i)
        for j in range(i + 1, len(arr)):
            count += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
    return arr, count


if __name__ == '__main__':
    arr_, count_ = selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(count_)
    print("sorted", arr_)
