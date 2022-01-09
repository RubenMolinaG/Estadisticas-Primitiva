from libreria_primitiva import *

'''
Resumen General:
    - Los números que más han salido -> (03/38/45/47/39/41)     // Ordenados de más a menos.
    - Los 3 números fijos que jugaremos siempre son -> (03/38/45)
    - Combinaciones de números que jugaremos en 2022:
        - Figura: 3/2/1, Numeros: [03 - 22 - 36 - 38 - 45 - 47]
        - Figura: 3/2/1, Numeros: [03 - 15 - 22 - 38 - 39 - 45]
        - Figura: 3/2/1, Numeros: [03 - 22 - 37 - 38 - 41 - 45]
        - Figura: 4/2/0, Numeros: [03 - 36 - 38 - 39 - 45 - 47]
'''

# Creamos el diccionario con los datos generales e históricos de la Primitiva.
diccionario_general = crear_diccionario()

with open('./data/historico_numero_apariciones.csv', 'r') as lectura:
    for linea in lectura:
        linea = linea.split(',')
        numero = linea[0]
        numero_repeticiones = int(linea[1])

        if numero in diccionario_general:
            diccionario_general[numero] = numero_repeticiones

# Creamos una copia del diccionario, ordenada, de más a menos apariciones.
diccionario_general_ordenado = ordenar_diccionario(diccionario_general)

# --------------------------------------------------------------------------
# Representamos graficamente el diccionario.
# --------------------------------------------------------------------------
dibujar_grafica(diccionario_general_ordenado)
dibujar_grafica(diccionario_general)
dibujar_grafica_plot(diccionario_general)