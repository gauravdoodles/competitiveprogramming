def partition (arr, low, high):

    pivot = arr[high];    # pivot

    i = (low - 1)         # Index of smaller element

    for j in range (low, high):

        #If current element is smaller than or

        # equal to pivot element

        if arr[j] <= pivot:

            #increment index of smaller element

            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)

 

def quicksort(arr, low, high):

    if low < high: 

        p = partition(arr, low, high)

        quicksort(arr, low, p - 1)

        quicksort(arr, p + 1, high)

 

arr = [5, 10, 8, 7, 3, 6, 12, 2, 7]

quicksort(arr, 0, len(arr)-1)

 

print("Sorted array:")

print(arr)