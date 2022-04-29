"""
Complexity O(n2) : Worst Case
Best Case O(n)
Space O(1)
"""


def bubble_sort(arr):
    swapped = False
    count = 0
    for i in range(0, len(arr)):
        print(i)
        for j in range(0, len(arr) - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(arr)
        if not swapped:
            break
    print(count)
    return arr


if __name__ == '__main__':
    arr_ = bubble_sort(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(arr_)
