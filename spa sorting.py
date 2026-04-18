def insertion_sort(arr):
    """Task 1.1: Sorts in non-decreasing order, O(n²), stable, in-place."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    """Task 1.2 helper: Stable merge for merge_sort."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result

def merge_sort(arr):
    """Task 1.2: O(n log n), stable, O(n) extra space."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def partition(arr, low, high):
    """Lomuto partition: last element pivot (recommended strategy)."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    """Task 1.3: Avg O(n log n), in-place. Recurse on partitions."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# REQUIRED Correctness Check - Run in VS Code
test_input = [5, 2, 9, 1, 5, 6]

# Insertion Sort Test
arr_insert = test_input[:]
insertion_sort(arr_insert)
print(f"Insertion: {arr_insert }")

# Merge Sort Test
arr_merge = test_input[:]
sorted_merge = merge_sort(arr_merge)
print(f"Merge:    {sorted_merge} ")

# Quick Sort Test
arr_quick = test_input[:]
quick_sort(arr_quick)
print(f"Quick:    {arr_quick} ")


### Task 2

## A

import time
import copy

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]; j -= 1
        arr[j + 1] = key

def merge(left, right):
    result = []; i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def partition(arr, low, high):
    pivot = arr[high]; i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1; arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def measure_time(sort_func, arr):
    arr_copy = copy.deepcopy(arr)  
    start_time = time.perf_counter()
    sort_func(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90] * 100  
    
   
    
    # Test each sort
    insert_time = measure_time(insertion_sort, test_data)
    merge_time = measure_time(merge_sort, test_data)
    quick_time = measure_time(quick_sort, test_data)
    
    print(f"Insertion Sort: {insert_time:.2f} ms")
    print(f"Merge Sort:    {merge_time:.2f} ms") 
    print(f"Quick Sort:    {quick_time:.2f} ms")
    

## B 

import random

def generate_datasets():
    random.seed(42) 
    sizes = [1000, 5000, 10000]
    datasets = {}
    
    for size in sizes:
        datasets[f'random_{size}'] = [random.randint(1, 100000) for _ in range(size)]
        
        datasets[f'sorted_{size}'] = list(range(1, size + 1))
        
        datasets[f'reverse_{size}'] = list(range(size, 0, -1))
    
    return datasets


if __name__ == "__main__":
    datasets = generate_datasets()
    for name, data in datasets.items():
        print(f"\n{name}:")
        print(f"  Size: {len(data):,} | Range: {min(data)}-{max(data)}")
        print(f"  Preview: {data[:8]}...")  
    

## C

import time
import random
import sys
import copy


sys.setrecursionlimit(20000)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def partition(arr, low, high):
    pivot = arr[high]; i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1; arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    stack = [(low, high)]  
    
    while stack:
        low, high = stack.pop()
        if low >= high: continue
        
        pi = partition(arr, low, high)
        if pi - 1 > low:
            stack.append((low, pi - 1))
        if high > pi + 1:
            stack.append((pi + 1, high))


def measure_time(sort_func, arr):
    arr_copy = arr[:]  
    start = time.perf_counter()
    sort_func(arr_copy)
    return (time.perf_counter() - start) * 1000

def generate_datasets():
    random.seed(42)
    sizes = [1000, 5000, 10000]
    datasets = {}
    for size in sizes:
        datasets[f'random_{size}'] = [random.randint(1, 100000) for _ in range(size)]
        datasets[f'sorted_{size}'] = list(range(1, size + 1))
        datasets[f'reverse_{size}'] = list(range(size, 0, -1))
    return datasets

def run_experiments():
    datasets = generate_datasets()
    algos = {'Insert': insertion_sort, 'Merge': merge_sort, 'Quick': quick_sort}
    
    print("\n📈 EXECUTION TIMES (ms)")
    print(f"{'Dataset':<13} {'Insert':>7} {'Merge':>7} {'Quick':>7}")
    print("-" * 45)
    
    for name, data in datasets.items():
        times = {k: measure_time(v, data) for k, v in algos.items()}
        print(f"{name:<13} {times['Insert']:>6.1f}   {times['Merge']:>6.1f}   {times['Quick']:>6.1f}")

if __name__ == "__main__":
    run_experiments()
    