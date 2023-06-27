# Nama : Rosanti
# Nim  : F55121027

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def print_iterations(arr):
    n = len(arr)
    print("5 iterasi pertama:")
    for i in range(min(5, n)):
        print(arr[i], end=" ")
    print("\n5 iterasi terakhir:")
    for i in range(max(0, n-5), n):
        print(arr[i], end=" ")
    print()

def analyze_algorithm(arr, algorithm):
    start_time = time.time()
    if algorithm == "bubble":
        bubble_sort(arr)
    elif algorithm == "insertion":
        insertion_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def display_results(before_sort, after_sort, execution_time):
    print("Waktu komputasi pengurutan:", execution_time, "sekon")
    print("Tampilan Before:", before_sort)
    print("Tampilan After:", after_sort)


# Main program
user_input = input("Pilih algoritma (bubble/insertion): ")
data = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

if user_input == "bubble":
    before_sort = list(data)
    execution_time = analyze_algorithm(data, "bubble")
    after_sort = list(data)
elif user_input == "insertion":
    before_sort = list(data)
    execution_time = analyze_algorithm(data, "insertion")
    after_sort = list(data)
else:
    print("Pilihan tidak valid")

print_iterations(after_sort)
display_results(before_sort, after_sort, execution_time)