from copy import deepcopy

# 1. Selection Sort
def selection_sort(vector):
    vec = deepcopy(vector)
    LEN  = len(vec)
    for i in range(LEN):
        min = i
        for j in range(i+1, LEN):
            if vec[j] < vec[min]:
                min = j
        vec[i], vec[min] = vec[min], vec[i]
    return vec



# 2. Bubble Sort
def bubble_sort(vector):
    vec = deepcopy(vector)
    LEN = len(vec)
    for i in range(LEN):
        for j in range(LEN-i-1):
            if vec[j] > vec[j+1]:
                vec[j], vec[j+1] = vec[j+1], vec[j]
    return vec



# 3. Insertion Sort
def insertion_sort(vector):
    vec = deepcopy(vector)
    LEN = len(vec)
    for i in range(1, LEN):
        key = vec[i]
        j = i-1
        while j >= 0 and key < vec[j]:
            vec[j+1], vec[j] = vec[j], vec[j+1]
            j -= 1
    return vec



# 4. Quick Sort
def quick_sort(vector):
    vec = deepcopy(vector)
    LEN = len(vec)
    if LEN <= 1:
        return vec

    pivot = vec[LEN//2]
    left = [x for x in vec if x < pivot]
    middle = [x for x in vec if x == pivot]
    right = [x for x in vec if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



# AUXILIARY FUNCTIONS
# Count Time Function
def count_time(func, vector):
    start = time()
    sorted_vector = func(vector)
    end = time()
    return end - start


# MAIN FUNCTION - EXAMPLE WITH 25 ELEMENTS
from time import time
from random import randrange

array = [randrange(1000) for i in range(25)]

start1 = time()
array1 = selection_sort(array)
end1 = time()
time1 = end1 - start1

start2 = time()
array2 = bubble_sort(array)
end2 = time()
time2 = end2 - start2

start3 = time()
array3 = insertion_sort(array)
end3 = time()
time3 = end3 - start3

start4 = time()
array4 = quick_sort(array)
end4 = time()
time4 = end4 - start4

print(f"Original Array: {array}\n\n")
print(f"Selection Sort: {array1} ({1000*time1} ms)")
print(f"Bubble Sort:    {array2} ({1000*time2} ms)")
print(f"Insertion Sort: {array3} ({1000*time3} ms)")
print(f"Quick Sort:     {array4} ({1000*time4} ms)")




# MAIN FUNCTION - EXAMPLE WITH 1000 ELEMENTS
from random import randrange
from time import time
from matplotlib import pyplot as plt
from copy import deepcopy

# Comparison of algorithms and number of elements
def run(num_elements, display_on=False):

    # Initialization
    vector = [randrange(10 * num_elements) for i in range(num_elements)]
    funcs = [selection_sort, bubble_sort, insertion_sort, quick_sort]
    times_elapsed = []

    # Compare the sorting algorithms
    print(100 * "-")
    print(f"Sorting a {len(vector)}-elements vector with:\n")
    for func in funcs:
        time_elapsed = count_time(func, vector)
        times_elapsed.append(time_elapsed)
        time_shown = f"{time_elapsed:.2f} seconds" if time_elapsed >= 0.1 else f"{1000*time_elapsed:.2f} ms"
        print(f"{func.__name__} ----> {time_shown}")

    # There is a choice to turn on the displays
    if display_on:
        print("\n")
        funcs_names = [func.__name__ for func in funcs]
        plt.bar(funcs_names, times_elapsed)
        plt.title(f"{num_elements} ELEMENTS")
        plt.ylabel("Time [seconds]")
        plt.show()
    print(100 * "-")
    print("\n\n")
    return times_elapsed



# Examples for various numbers of elements
# Initialization
num_elements_list = [100, 200, 500, 1000, 2000, 5000, 10000]
flags_list = len(num_elements_list) * [False]
flags_list[3] = True
funcs = [selection_sort, bubble_sort, insertion_sort, quick_sort]
funcs_names = [func.__name__ for func in funcs]
TIMES_MATRIX = [[0 for __ in range(len(funcs))] for _ in range(len(num_elements_list))]

for i in range(len(num_elements_list)):
    num_elements = num_elements_list[i]
    display_on = flags_list[i]
    times_elapsed = run(num_elements, display_on)
    TIMES_MATRIX[i] = times_elapsed
print(TIMES_MATRIX)

# Comparison of algorithms
import seaborn as sns
sns.set_style("darkgrid")

for j in range(len(funcs)):
    trend = list()
    for i in range(len(num_elements_list)):
        trend.append(TIMES_MATRIX[i][j])
    sns.lineplot(x=num_elements_list, y=trend, label=funcs_names[j])

plt.legend()
plt.title("Comparison of algorithms")
plt.xlabel("Number of elements")
plt.ylabel("Time [seconds]")
plt.show()


import pandas as pd
df = pd.DataFrame(TIMES_MATRIX, index=num_elements_list, columns=funcs_names)
print(df)
[ROWS, COLS] = df.shape
df2 = df.iloc[ROWS-2:ROWS]
print(df2)
sns.heatmap(df2, annot=True, cmap="Blues")
plt.show()
