"""
Punto de entrada principal del proyecto. 
Permite seleccionar la demo de word_counter o la demo de stack_queue_menu.
"""
from services.word_counter import main_word_counter_demo
from services.stack_queue_menu import main_menu_demo
from services.searching import searching_demo
from services.sorting import sorting_demo


def main():
    
    while True:
        print("\n=== Proyecto Algoritmos - Menu Principal ===")
        print("1. Contar palabras")
        print("2. Menú Pila y Cola")
        print("3. Demostración de búsqueda")
        print("4. Demostración de ordenamiento")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            main_word_counter_demo()
        elif opcion == "2":
            main_menu_demo()
        elif opcion == "3":
            searching_demo()
        elif opcion == "4":
            sorting_demo()    
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, vuelva intentar.")

if __name__ == "__main__":
    main()            
