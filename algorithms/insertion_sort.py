import copy


def insertion_sort(arr):
    arr1 = copy.deepcopy(arr)
    count = 0
    for i in range(1, len(arr)):
        count += 1
        temp = arr[i]
        print(f"ith arr[{i}]={arr[i]}")
        if arr[i-1] > temp:
            for j in range(i-1, -1, -1):
                count += 1
                print(f"Jth arr[{j}]={arr[j]}")
                if arr[j] > temp:
                    arr[j+1] = arr[j]
                    arr[j] = temp
                else:
                    break
        print(arr)
    print(arr)
    print(count)
    new_count = 0
    for i in range(1, len(arr1)):
        new_count += 1
        key = arr1[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr1[j]:
            new_count += 1
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
    print(arr1)
    print(new_count)


if __name__ == '__main__':
    # insertion_sort([8, 4, 6, 3, 1, 7, 5, 9, 2])
    insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])