from .Algorithms import (
    MergeSort,
    BubbleSort,
    InsertionSort,
    HeapSort,
    QuickSort,
    SelectionSort
)

if __name__ == "__main__":
    array = []
    merge_sort = MergeSort(array)
    buble_sort = BubbleSort(array)
    insertion_sort = InsertionSort()
    heap_sort = HeapSort()
    quick_sort = QuickSort()
    selection_sort = SelectionSort()