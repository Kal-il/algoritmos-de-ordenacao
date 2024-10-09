# Merge Sort

class MergeSort:
    def __init__(self, arr):
        self.arr = arr

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

    def sort(self):
        self.merge_sort()
        return self.arr

# Bubble Sort

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr) - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.data

# Insertion Sort

class InsertionSort:
    def __init__(self):
        pass

    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

# Selection Sort

class SelectionSort:
    def sort(self, data):
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

# Quick Sort

class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def quick_sort(self):
        self._quick_sort_helper(0, len(self.arr) - 1)

    def _quick_sort_helper(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            self._quick_sort_helper(low, pivot_index - 1)
            self._quick_sort_helper(pivot_index + 1, high)

    def _partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def sort(self):
        self.quick_sort()
        return self.arr

# Heap Sort

class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heap_sort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self._heapify(i, 0)

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[i] < self.arr[left]:
            largest = left

        if right < n and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self._heapify(n, largest)

    def sort(self):
        self.heap_sort()
        return self.arr