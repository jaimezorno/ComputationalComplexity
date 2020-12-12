

def selection_sort_func(array):
    """
    Selection sort algorithm to
    sort a given array of integers

    :param array: input array to the algorithm
    :return: array: array sorted after process
    """

    # Parametrize the length of the array
    array_len = len(array)
    # Find the minimum element in remaining array
    for i in range(array_len):
        min_index = i
        for j in range(i+1, array_len):
            if array[min_index] > array[j]:
                min_index = j

        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

    return array
