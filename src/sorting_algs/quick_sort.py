
import numpy as np


def partition(array, low, high):
    """
    Function that takes the last element as pivot
    places the pivot element at is correct position
    in the sorted array, and places all smaller elements
    to the left, and greater to the right

    :param array: array to sort
    :param low: smaller element
    :param high: bigger element
    :return: index where partition must occur
    """
    # index of smaller element
    i = (low -1)
    # Calculate pivot at random
    pivot_index = np.random.randint(low=0, high=len(array))
    pivot = array[pivot_index]

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:

            # increment index of smaller element
            i = i+ 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


def quick_sort_func(array, low, high):
    """
    function that implements the quicksort
    sorting algorithm
    :param array: array to sort
    :return:
    """
    if len(array) == 1:
        return array
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(array, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort_func(array, low, pi - 1)
        quick_sort_func(array, pi + 1, high)
