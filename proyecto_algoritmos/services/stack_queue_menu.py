"""
Módulo que define un menú de consola para operar con una Pila y una Cola.
Se separa la lógica de la interfaz (input/print) en funciones específicas.
"""
from collections import deque

def push_stack(stack, item):
    """
    Operación para apilar un elemento (push).
    Complejidad: O(1) amortizado con list en Python.
    """
    stack.append(item)
    print(f"Elemento '{item}' agregado a la pila.")

def pop_stack(stack):
    """
    Operación para desapilar un elemento (pop).
    Complejidad: O(1) amortizado con list en Python.
    """
    if stack:
        removed = stack.pop()
        print(f"Elemento '{removed}' removido de la pila.")
    else:
        print("La pila está vacía.")

def enqueue(queue, item):
    """
    Operación para encolar un elemento.
    Complejidad: O(1) con deque.
    """
    queue.append(item)
    print(f"Elemento '{item}' encolado.")

def dequeue(queue):
    """
    Operación para desencolar un elemento.
    Complejidad: O(1) con deque.
    """
    if queue:
        removed = queue.popleft() # se elimina el primer elemento
        print(f"Elemento '{removed}' desencolado.")
    else:
        print("La cola está vacía.")

def run_stack_queue_menu():
    """
    Muestra un menú en consola para interactuar con una Pila y una Cola.
    Usa funciones separadas para cada operación para mantener buen diseño.
    """
    stack = []  # Implementación de pila usando lista (LIFO)
    queue = deque() # Implementación de cola usando deque (FIFO)

    while True:
        print("\n===== Menú Stack & Queue =====")
        print("1. Push (Pila)")
        print("2. Pop (Pila)")
        print("3. Enqueue (Cola)")
        print("4. Dequeue (Cola)")
        print("5. Ver estado de Pila y Cola")
        print("0. Salir")

        opcion = input("elige una opción: ")

        if opcion == "1":
            item = input("Ingrese el elemento a apilar: ")
            push_stack(stack, item)

        elif opcion == "2":
            pop_stack(stack)

        elif opcion == "3":
            item = input("Ingrese el elemento a la queue: ")
            enqueue(queue, item)

        elif opcion == "4":
            dequeue(queue)

        elif opcion == "5":
            print(f"Pila (top -> bottom): {list(reversed(stack))}")
            print(f"Cola (front -> back): {list(queue)}")

        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, vuelva intentar.")

def main_menu_demo():
    #Punto de entrada rápido para mostar el menú en acción

    run_stack_queue_menu()

if __name__ == "__main__":
    main_menu_demo()    
            
