import random

# Bubble Sort
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.swaps = 0        # Para contar trocas

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr) - 1):
                self.comparisons += 1  # Contando a comparação
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    self.swaps += 1  # Contando a troca
        return self.arr, self.comparisons, self.swaps

# Selection Sort
class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.swaps = 0        # Para contar trocas
    
    def sort(self):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                self.comparisons += 1  # Contando a comparação
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            if min_index != i:
                self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
                self.swaps += 1  # Contando a troca
        return self.arr, self.comparisons, self.swaps

# Insertion Sort
class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.swaps = 0        # Para contar trocas

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0:
                self.comparisons += 1  # Contando a comparação
                if key < self.arr[j]:
                    self.arr[j + 1] = self.arr[j]
                    self.swaps += 1  # Contando a troca
                    j -= 1
                else:
                    break
            self.arr[j + 1] = key
        return self.arr, self.comparisons, self.swaps

# Merge Sort
class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.assignments = 0  # Para contar atribuições (em vez de trocas)

    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                self.comparisons += 1  # Contando a comparação
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    self.assignments += 1  # Contando a atribuição
                    i += 1
                else:
                    arr[k] = right_half[j]
                    self.assignments += 1  # Contando a atribuição
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                self.assignments += 1  # Contando a atribuição
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                self.assignments += 1  # Contando a atribuição
                j += 1
                k += 1

    def sort(self):
        self.merge_sort()
        return self.arr, self.comparisons, self.assignments


# Quick Sort
class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.swaps = 0        # Para contar trocas

    def quick_sort(self):
        self._quick_sort_helper(0, len(self.arr) - 1)

    def _quick_sort_helper(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            self._quick_sort_helper(low, pivot_index - 1)
            self._quick_sort_helper(pivot_index + 1, high)

    def _partition(self, low, high):
        random_pivot = random.randint(low, high)
        self.arr[high], self.arr[random_pivot] = self.arr[random_pivot], self.arr[high]
        self.swaps += 1  # Contando a troca

        pivot = self.arr[high]
        i = low - 1

        for j in range(low, high):
            self.comparisons += 1  # Contando a comparação
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.swaps += 1  # Contando a troca

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        self.swaps += 1  # Contando a troca
        return i + 1

    def sort(self):
        self.quick_sort()
        return self.arr, self.comparisons, self.swaps

# Heap Sort
class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # Para contar comparações
        self.swaps = 0        # Para contar trocas

    def heap_sort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.swaps += 1  # Contando a troca
            self._heapify(i, 0)

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1  # Contando a comparação
            if self.arr[i] < self.arr[left]:
                largest = left

        if right < n:
            self.comparisons += 1  # Contando a comparação
            if self.arr[largest] < self.arr[right]:
                largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.swaps += 1  # Contando a troca
            self._heapify(n, largest)

    def sort(self):
        self.heap_sort()
        return self.arr, self.comparisons, self.swaps