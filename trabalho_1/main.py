import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate
from Algorithms import (
    MergeSort,
    BubbleSort,
    InsertionSort,
    HeapSort,
    QuickSort,
    SelectionSort
)

def run_and_measure(algorithm, array):
    start_time = time.time()
    sorted_array, comparisons, swaps = algorithm.sort()
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Converter para milissegundos
    return elapsed_time, comparisons, swaps

# Funções para gerar listas
def generate_ordered_list(size):
    return list(range(size))


def generate_reverse_ordered_list(size):
    return list(range(size, 0, -1))


def generate_random_list(size):
    return random.sample(range(size * 2), size)

def runfn(alg_name, AlgClass):
    sizes = [1000, 10000, 50000, 100000] 
    vetor_ordenada = []
    vetor_inversa = []
    vetor_randomica = []# Tamanhos das listas
    vetor_compara_ord = []
    vetor_compara_inv = []
    vetor_compara_rand = []
    vetor_trocas_ord = []
    vetor_trocas_inv = []
    vetor_trocas_rand = []
    
    print(f"\n\n+-----------------------------------------------------------------+\nExecutando {alg_name}...\n")
    # Gerando as listas: 
    for size in sizes:
        ordered_list = generate_ordered_list(size)
        reverse_ordered_list = generate_reverse_ordered_list(size)
        random_list = generate_random_list(size)
        
        print(f'\n{alg_name} com lista de {size} itens')

        # Ordenada
        alg_instance = AlgClass(ordered_list[:])  # Passar uma cópia da lista
        time_taken_ord, comparisons_ord, swaps_ord = run_and_measure(alg_instance, ordered_list[:])
        # print(f"Ordenada: {time_taken_ord:.6f} ms, {comparisons_ord} comparações, {swaps_ord} trocas")

        # Inversamente ordenada
        alg_instance = AlgClass(reverse_ordered_list[:])
        time_taken_inv, comparisons_inv, swaps_inv = run_and_measure(alg_instance, reverse_ordered_list[:])
        # print(f"Inversamente ordenada: {time_taken_inv:.6f} ms, {comparisons_inv} comparações, {swaps_inv} trocas")

        # Aleatória
        alg_instance = AlgClass(random_list[:])
        time_taken_rand, comparisons_rand, swaps_rand = run_and_measure(alg_instance, random_list[:])
        # print(f"Aleatória: {time_taken_rand:.6f} ms, {comparisons_rand} comparações, {swaps_rand} trocas")
        
        table = [
            ["Tipo de Lista", "Tempo (ms)", "Comparações", "Trocas"],
            ["Ordenada", f"{time_taken_ord:.6f}", comparisons_ord, swaps_ord],
            ["Inversamente Ordenada", f"{time_taken_inv:.6f}", comparisons_inv, swaps_inv],
            ["Aleatória", f"{time_taken_rand:.6f}", comparisons_rand, swaps_rand],
        ]

        # Exibir a tabela formatada
        print(tabulate(table, headers="firstrow", tablefmt="grid"))

        vetor_ordenada.append(time_taken_ord)
        vetor_inversa.append(time_taken_inv)
        vetor_randomica.append(time_taken_rand)
        vetor_compara_ord.append(comparisons_ord)
        vetor_compara_inv.append(comparisons_inv)
        vetor_compara_rand.append(comparisons_rand)
        vetor_trocas_ord.append(swaps_ord)
        vetor_trocas_inv.append(swaps_inv)
        vetor_trocas_rand.append(swaps_rand)
        
    return vetor_ordenada, vetor_inversa, vetor_randomica, vetor_compara_ord, vetor_trocas_ord, vetor_compara_inv, vetor_trocas_inv, vetor_compara_rand, vetor_trocas_rand

def plotfunc(x, y_ord, y_inv, y_rand, alg_name):
    plt.figure(figsize=(10, 6))
    
    # Usar cores e estilos diferentes para as linhas
    plt.plot(x, y_ord, label='Ordenada', color='blue', marker='o')
    plt.plot(x, y_inv, label='Inversamente Ordenada', color='red', marker='s')
    plt.plot(x, y_rand, label='Aleatória', color='green', marker='^')
    
    # Adicionar título e legendas
    plt.title(f'Tempo de execução x Tamanho da lista ({alg_name})', fontsize=14)
    plt.xlabel('Tamanho da lista', fontsize=12)
    plt.ylabel('Tempo de execução (ms)', fontsize=12)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=3)
    plt.grid(True)
    
    # Anotando o valor inicial e final para cada curva
    plt.annotate(f'{y_ord[0]:.2f} ms', (x[0], y_ord[0]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{y_ord[-1]:.2f} ms', (x[-1], y_ord[-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    
    plt.annotate(f'{y_inv[0]:.2f} ms', (x[0], y_inv[0]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{y_inv[-1]:.2f} ms', (x[-1], y_inv[-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    
    plt.annotate(f'{y_rand[0]:.2f} ms', (x[0], y_rand[0]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{y_rand[-1]:.2f} ms', (x[-1], y_rand[-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig(f'grafico_{alg_name}.png', format='png', bbox_inches='tight')
    
# função para plotar comparações e trocas

def plot_comparisons_and_swaps(x, comparisons_ord, swaps_ord, comparisons_inv, swaps_inv, comparisons_rand, swaps_rand, algorithm_name):
    plt.figure(figsize=(10, 10))

    # Subplot para Comparações
    plt.subplot(2, 1, 1)
    bar_width = 0.25  # Largura das barras
    x_indices = range(len(x))

    # Criando as barras para comparações
    plt.bar([i - bar_width for i in x_indices], comparisons_ord, width=bar_width, label='Comparações (Ordenada)', color='blue')
    plt.bar(x_indices, comparisons_inv, width=bar_width, label='Comparações (Inversa)', color='red')
    plt.bar([i + bar_width for i in x_indices], comparisons_rand, width=bar_width, label='Comparações (Aleatória)', color='green')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=3)
    plt.grid(axis='y')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Número de Comparações')
    plt.title(f'Comparações - {algorithm_name}')
    plt.xticks(x_indices, x)  # Definindo os rótulos do eixo x

    # Subplot para Trocas
    plt.subplot(2, 1, 2)
    
    # Criando as barras para trocas
    plt.bar([i - bar_width for i in x_indices], swaps_ord, width=bar_width, label='Trocas (Ordenada)', color='blue')
    plt.bar(x_indices, swaps_inv, width=bar_width, label='Trocas (Inversa)', color='red')
    plt.bar([i + bar_width for i in x_indices], swaps_rand, width=bar_width, label='Trocas (Aleatória)', color='green')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=3)
    plt.grid(axis='y')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Número de Trocas')
    plt.title(f'Trocas - {algorithm_name}')
    plt.xticks(x_indices, x)  # Definindo os rótulos do eixo x

    plt.tight_layout()
    plt.savefig(f'grafico_{algorithm_name}_comparisons_swaps.png', format='png', bbox_inches='tight')




    
if __name__ == "__main__":
    
    algorithms = [
        ('Bubble Sort', BubbleSort),
        ('Selection Sort', SelectionSort),
        ('Insertion Sort', InsertionSort),
        ('Merge Sort', MergeSort),
        ('Quick Sort', QuickSort),
        ('Heap Sort', HeapSort)
    ]
    
    # Tamanhos de listas a serem testadas
    sizes = [1000, 10000, 50000, 100000]
    
    for alg_name, AlgClass in algorithms:
        vetor_ordenada, vetor_inversa, vetor_randomica, vetor_compara_ord, vetor_trocas_ord, vetor_compara_inv, vetor_trocas_inv, vetor_compara_rand, vetor_trocas_rand = runfn(alg_name=alg_name, AlgClass=AlgClass)
        plotfunc(sizes, vetor_ordenada, vetor_inversa, vetor_randomica, alg_name=alg_name)
        plot_comparisons_and_swaps(sizes, vetor_compara_ord, vetor_trocas_ord, vetor_compara_inv, vetor_trocas_inv, vetor_compara_rand, vetor_trocas_rand, alg_name)
        