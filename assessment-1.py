import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

def insertion_sort(arr):
    res = arr[:]
    for i in range(1, len(res)):
        key = res[i]
        j = i - 1
        while j >= 0 and res[j] > key:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = key
    return res

def test_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    print(f"{'Size':>8} | {'Merge Sort':>12} | {'Insertion':>12} | {'Timsort':>12}")
    print('-' * 55)
    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        # Merge Sort
        t_merge = timeit.timeit(lambda: merge_sort(arr), number=1)

        # Insertion Sort
        if size <= 1000:
            t_insert = timeit.timeit(lambda: insertion_sort(arr), number=1)
        else:
            t_insert = float('nan')

        # Timsort
        t_tim = timeit.timeit(lambda: sorted(arr), number=1)

        print(f"{size:8d} | {t_merge:12.6f} | {t_insert:12.6f} | {t_tim:12.6f}")

test_sorting_algorithms()