def merge(left, right):

    left_length = len(left)

    right_length = len(right)

 

    array = []

    i = 0

    j = 0

 

    while i < left_length and j < right_length:

        if left[i] < right[j]:

            array.append(left[i])

            i += 1

        else:

            array.append(right[j])

            j += 1

 

    while i < left_length:

        array.append(left[i])

        i += 1

 

    while j < right_length:

        array.append(right[j])

        j += 1

 

    return array

 

def merge_sort(array):

    length = len(array)

 

    # base case

    if length <= 1: return array

 

    # recursion

    midpoint = length // 2

    left_half = merge_sort(array[:midpoint])

    right_half = merge_sort(array[midpoint:])

    return merge(left_half, right_half)

 

array = [10, 20, 5, 8, 7, 2, 15, 12]

print("Initial array:", array)

print("Sorted array:", merge_sort(array))