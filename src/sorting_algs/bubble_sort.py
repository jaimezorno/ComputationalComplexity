

def bubble_sort_func(array):
    """
    Bubble sort algorithm to
    sort a given array of integers
    :param array: input array to the algorithm
    :return: array: array sorted after process
    """

    # Calculate the length of the array
    n = len(array)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
