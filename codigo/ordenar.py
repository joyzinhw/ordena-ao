import random
import time
import pandas

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def generate_arrays(size):
    crescente = list(range(size))
    decrescente = list(range(size, 0, -1))
    aleatorio = random.sample(range(size * 2), size)
    return crescente, decrescente, aleatorio

def test_sorting_algorithm(sort_func, input_data):
    times = []
    for _ in range(3):
        arr = input_data.copy()
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / 3

sizes = [1000, 5000, 10000, 20000, 30000]

for size in sizes:
    print(f"Tamanho do vetor: {size}")
    crescente, decrescente, aleatorio = generate_arrays(size)

    for sort_name, sort_func in [("Insertion Sort", insertion_sort), ("Merge Sort", merge_sort), ("Bubble Sort", bubble_sort)]:
        print(f"Algoritmo de ordenação: {sort_name}")
        
        avg_time = test_sorting_algorithm(sort_func, crescente)
        print(f"Ordem crescente: Tempo médio = {avg_time:.6f} segundos")

       
        avg_time = test_sorting_algorithm(sort_func, decrescente)
        print(f"Ordem decrescente: Tempo médio = {avg_time:.6f} segundos")

        avg_time = test_sorting_algorithm(sort_func, aleatorio)
        print(f"Ordem aleatória: Tempo médio = {avg_time:.6f} segundos")

        print()

      
