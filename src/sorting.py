import numpy as np
import time
from sorting_algs import selection_sort, bubble_sort, quick_sort

max_value = 20000


input_size = 5000
random_array_1 = np.random.randint(low=0, high=max_value, size=input_size)

###  Selection Sort
start = time.time()
sorted_array = selection_sort.selection_sort_func(random_array_1)
end = time.time()

print("Selection Sort")
print(f"For an input of size {input_size} the algorithm took {end - start}ms to execute")

input_size = 10000
random_array_2 = np.random.randint(low=0, high=max_value, size=input_size)

start = time.time()
sorted_array = selection_sort.selection_sort_func(random_array_2)
end = time.time()

print(f"For an input of size {input_size} the algorithm took {end - start}ms to execute")

###  Bubble sort
start = time.time()
sorted_array = bubble_sort.bubble_sort_func(random_array_1)
end = time.time()

print("Bubble Sort")
print(f"For an input of size {len(random_array_1)} the algorithm took {end - start}ms to execute")

start = time.time()
sorted_array = bubble_sort.bubble_sort_func(random_array_2)
end = time.time()

print(f"For an input of size {len(random_array_2)} the algorithm took {end - start}ms to execute")

###  Quick Sort
start = time.time()
sorted_array = quick_sort.quick_sort_func(random_array_1, 0, len(random_array_1)-1)
end = time.time()

print("Quick Sort")
print(f"For an input of size {len(random_array_1)} the algorithm took {end - start}ms to execute")

start = time.time()
sorted_array = quick_sort.quick_sort_func(random_array_2, 0, len(random_array_2)-1)
end = time.time()

print(f"For an input of size {len(random_array_2)} the algorithm took {end - start}ms to execute")