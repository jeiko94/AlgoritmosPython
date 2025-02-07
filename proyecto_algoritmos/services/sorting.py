#Contendrá implementaciones de bubble sort, insertion sort y al menos merge sort o quick sort.
#Implementaciones de algoritmos de ordenamiento clásicos en Python.

"""
Bubble sort compara pares adyacentes y los intercambia si estan en orden incorrecto.

:parametro arr: lista de elementos. (se ordenan en el lugar)
:return: None (la lista se ordena en el lugar)

Complejidad O(n^2): en promedio y en el peor de los casos.

por que funciona:
    - en cada pasada, el elemento mas grande "flota" hasta su posición correcta al final.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # últimos i ya estan en su sitio
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
"""
Insertion sort: construye gradualmente una sublista ordenada a la izquierda.

:parametro arr: Lista de elemento se ordena en el lugar.
:return: None 

Complejidad O(n^2): en promedio y en el peor de los casos.

por que funciona:
    - En cada iteración, un elemento se "inserta" en su posición correcta en la sublista ordenada.
    - La sublista ordenada crece en 1 elemento en cada iteración.
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #Mover elemento mayor a 'key' una posición adelante de su posición actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

"""
    Merge Sort: divide el arreglo en mitades, las ordena recursivamente y luego las mezcla.
    
    :param arr: Lista de elementos (se ordena en el lugar usando sublistas temporales).
    :return: None
    
    Complejidad: O(n log n) en promedio y peor caso.
    
    Por qué funciona:
      - Divide & Conquer: descompone en sublistas cada vez más pequeñas hasta que son triviales de ordenar,
        luego combina (merge) las sublistas ordenadas en una lista final ordenada.        
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #ordenar recuersivamente las mitades
        merge_sort(left_half)
        merge_sort(right_half)
        # Mezclar (merge) ambas mitades
        i = 0  # índice para left_half
        j = 0  # índice para right_half
        k = 0  # índice para arr original
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copiar cualquier elemento restante de left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copiar cualquier elemento restante de right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def sorting_demo():
    """
    Demostración de los algoritmos de ordenamiento. cambios
    """
    data_bubble = [34, 2, 78, 1, 56, 9]
    data_insertion = [34, 2, 78, 1, 56, 9]
    data_merge = [34, 2, 78, 1, 56, 9]
    
    print("=== Bubble Sort ===")
    bubble_sort(data_bubble)
    print(f"Ordenado con Bubble Sort: {data_bubble}")
    
    print("\n=== Insertion Sort ===")
    insertion_sort(data_insertion)
    print(f"Ordenado con Insertion Sort: {data_insertion}")
    
    print("\n=== Merge Sort ===")
    merge_sort(data_merge)
    print(f"Ordenado con Merge Sort: {data_merge}")

if __name__ == "__main__":
    sorting_demo()