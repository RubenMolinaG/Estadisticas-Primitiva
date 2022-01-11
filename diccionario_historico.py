from libreria_primitiva import *

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
