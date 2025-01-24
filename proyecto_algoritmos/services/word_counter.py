"""
Módulo para contar la frecuencia de palabras.
Separación de responsabilidades:
- Lógica de conteo en una función dedicada.
- Posibilidad de reutilizar el código en otros módulos/proyectos.
"""
def count_words(word_list):
    """
    Cuenta la frecuencia de cada palabra en la lista

    :param word_list: lista de palabras
    :return: diccionario con la frecuencia de cada palabra {palabra: frecuencia}

    complejidad
    - Iteramos una vez sobre la lista de palabras => O(n), donde n = len(word_list)
    - Insertamos/buscar en dict es O(1) en promedio (hashing) => complejidad O(n) en total
    """
    frequency = {}

    for word in word_list:
        #Convierte la palabra a minuscula para normalizar
        word_lower = word.lower()

        #Insercción / actualización en el diccionario
        if word_lower in frequency:
            frequency[word_lower] += 1
        else:
            frequency[word_lower] = 1

    return frequency

def display_frequencies(freq_dict):
    """
    Muestra en consola la frecuencia de cada palabra

    :param freq_dict: Diccionario {palabra: frecuencia}
    :return: None

    """
    print("==== Frecuencia de palabras ====")
    for word, freq in freq_dict.items():
        print(f"{word}: {freq}")

    print("================================")

def main_word_counter_demo():
    """
    Función de demostración rápida para probar count_words y display_frequencies.
    """
    sample_words = ["Hola", "mundo", "hola", "python", "Mundo", "PYTHON", "hola", "prueba"] #Lista

    freq = count_words(sample_words)
    display_frequencies(freq)

if __name__ == "__main__":
    main_word_counter_demo()    