def binary_search(array, target):

    # requirement: array is sorted

    # returns the smallest index such that array[index] >= target

    # if all values are < target, returns len(array)

    low = 0

    high = len(array)

    while high - low > 1:

        mid = int((high + low) / 2)

        if array[mid] < target:

             low = mid

        else:

            high = mid

    return high

value = 5

arr = [2, 3, 5, 6, 7, 8, 10, 12, 15]

print("Value " + str(value) + " found at index " + str(binary_search(arr, value)))