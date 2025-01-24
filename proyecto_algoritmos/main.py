"""
Punto de entrada principal del proyecto. 
Permite seleccionar la demo de word_counter o la demo de stack_queue_menu.
"""
from services.word_counter import main_word_counter_demo
from services.stack_queue_menu import main_menu_demo

def main():
    
    while True:
        print("\n=== Proyecto Algoritmos - Menu Principal ===")
        print("1. Contar palabras")
        print("2. Menú Pila y Cola")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            main_word_counter_demo()
        elif opcion == "2":
            main_menu_demo()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()            
