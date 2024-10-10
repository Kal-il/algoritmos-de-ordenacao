def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1  # Incrementa o número de comparações
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1  # Incrementa o número de trocas
    return arr, comparacoes, trocas

# Testando o algoritmo
lista = [64, 34, 25, 12, 22, 11, 90]
sorted_list, num_comparacoes, num_trocas = bubble_sort(lista)

print(f"Lista ordenada: {sorted_list}")
print(f"Número de comparações: {num_comparacoes}")
print(f"Número de trocas: {num_trocas}")
