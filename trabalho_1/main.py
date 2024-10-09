import random
import time
from Algorithms import (
    MergeSort,
    BubbleSort,
    InsertionSort,
    HeapSort,
    QuickSort,
    SelectionSort
)


# Função para medir tempo e contagem de operações
def run_and_measure(algorithm, array):
    start_time = time.time()
    sorted_array = algorithm.sort()
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Converter para milissegundos
    return elapsed_time, sorted_array


# Funções para gerar listas
def generate_ordered_list(size):
    return list(range(size))


def generate_reverse_ordered_list(size):
    return list(range(size, 0, -1))


def generate_random_list(size):
    return random.sample(range(size * 2), size)


if __name__ == "__main__":
    sizes = [1000, 10000, 50000, 100000]  # Tamanhos das listas
    algorithms = [
        ('Bubble Sort', BubbleSort),
        ('Selection Sort', SelectionSort),
        ('Insertion Sort', InsertionSort),
        ('Merge Sort', MergeSort),
        ('Quick Sort', QuickSort),
        ('Heap Sort', HeapSort)
    ]

    # Loop pelos tamanhos de listas
    for size in sizes:
        print(f"Testando com lista de tamanho {size}...")

        # Gerar as listas
        ordered_list = generate_ordered_list(size)
        reverse_ordered_list = generate_reverse_ordered_list(size)
        random_list = generate_random_list(size)

        for alg_name, AlgClass in algorithms:
            print(f"\nExecutando {alg_name}...")

            # Ordenada
            alg_instance = AlgClass(ordered_list[:])  # Passar uma cópia da lista
            time_taken, _ = run_and_measure(alg_instance, ordered_list[:])
            print(f"Ordenada: {time_taken:.2f} ms")

            # Inversamente ordenada
            alg_instance = AlgClass(reverse_ordered_list[:])
            time_taken, _ = run_and_measure(alg_instance, reverse_ordered_list[:])
            print(f"Inversamente ordenada: {time_taken:.2f} ms")

            # Aleatória
            alg_instance = AlgClass(random_list[:])
            time_taken, _ = run_and_measure(alg_instance, random_list[:])
            print(f"Aleatória: {time_taken:.2f} ms")
