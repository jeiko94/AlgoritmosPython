#Contendrá implementaciones de búsqueda lineal y búsqueda binaria con ejemplos.
"""
    :parametro arr: lista de elementos.
    :parametro target: elemento a buscar.
    return: indice del 'target' si se encuentra, -1 en caso contrario.

    complejidad de tiempo: O(n)
    complejidad de espacio: O(1)
    por que funciona:
        - Compara secuencialmente cada elemento de la lista con el 'target'.
        - se detiene al encontrarlo (o al llegar al final de la lista).
    """
def linear_search(arr, target):
    
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


"""
Busqueda binaria: requiere arr ordenado.

:parametro arr: lista de elementos ordenados.
:parametro target: elemento a buscar.
return: indice del 'target' si se encuentra, -1 en caso contrario.

complejidad de tiempo: O(log(n))
complejidad de espacio: O(1)

por que funciona:
    - Divide la lista en dos mitades y compara el 'target' con el elemento en el medio.
    - Si el 'target' es menor, se busca en la mitad izquierda.
    - Si el 'target' es mayor, se busca en la mitad derecha.
    - Se repite el proceso hasta encontrar el 'target' o hasta que la lista se reduzca a 0 elementos.
"""
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Demostración de uso de las funciones de búsqueda
def searching_demo():
    data = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]

    print("==== Búsqueda lineal ====")
    index_lin = linear_search(data, 5)
    print(f"Búsqueda lineal de 5 -> índice: {index_lin}")

    print("\n=== Búsqueda Binaria ===")
    # data está ordenado, podemos usar binary_search
    index_bin = binary_search(data, 5)
    print(f"Búsqueda binaria de 5 -> índice: {index_bin}")

if __name__ == "__main__":
    searching_demo()    